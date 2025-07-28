"""
runner.py  ·  CrewAI Pipeline Launcher
------------------------------------------------
20250720 新增功能
1. --direct_topic  ：跳過 generate_topics，直接以指定主題進行後續 Research→Writer 流程
2. GoogleTrendsTool 後備實作（若 crewai_tools 尚未內建）
"""

import argparse, os, textwrap, yaml, re
from datetime import datetime

from dotenv import load_dotenv
from crewai import Agent, Task, Crew


# 可選工具 (如有更多工具在此擴充)
from crewai_tools import SerperDevTool, WebsiteSearchTool


# ========= Artifact Logging ================
import os, json, shutil, uuid, datetime, sys, subprocess, atexit, io,  warnings

class ArtifactLogger:
    """
    建立 runs/{run_id}/ 目錄，並提供簡易 API
      • save_inputs(dict)
      • save_env()
      • save_task_output(task_name, content:str)
      • close()  # flush console capture
    """
    def __init__(self, base_dir: str = "runs"):
        ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        rand = uuid.uuid4().hex[:6]
        self.run_id = f"{ts}-{rand}"
        self.run_dir = os.path.join(base_dir, self.run_id)
        self.out_dir = os.path.join(self.run_dir, "outputs")
        os.makedirs(self.out_dir, exist_ok=True)

        # 攔截 stdout 以便寫入 console.log
        self._stdout_orig = sys.stdout
        self._buffer = io.StringIO()
        sys.stdout = self._buffer    # redirect

        atexit.register(self.close)  # 保證異常退出也 flush

    # ---------- public helpers ----------
    def save_inputs(self, data: dict):
        with open(os.path.join(self.run_dir, "inputs.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def save_env(self):
        env = {
            "python": sys.version,
            "git_commit": self._get_git_commit(),
            "packages": self._pip_freeze_hash()
        }
        with open(os.path.join(self.run_dir, "env.json"), "w", encoding="utf-8") as f:
            json.dump(env, f, ensure_ascii=False, indent=2)

    def save_task_output(self, task_name: str, content: str):
        fname = f"{task_name}.md"
        with open(os.path.join(self.out_dir, fname), "w", encoding="utf-8") as f:
            f.write(content)

    def close(self):
        # 將攔截的 console 內容寫入檔
        sys.stdout = self._stdout_orig
        log_path = os.path.join(self.run_dir, "console.log")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(self._buffer.getvalue())
        self._buffer.close()

    # ---------- private helpers ----------
    def _get_git_commit(self):
        try:
            return subprocess.check_output(
                ["git", "rev-parse", "--short", "HEAD"],
                stderr=subprocess.DEVNULL
            ).decode().strip()
        except Exception:
            return "N/A"

    def _pip_freeze_hash(self):
        try:
            pkgs = subprocess.check_output(
                [sys.executable, "-m", "pip", "freeze"],
                stderr=subprocess.DEVNULL
            ).decode().splitlines()
            return hash("\n".join(pkgs))
        except Exception:
            return "N/A"


warnings.filterwarnings(
    "ignore",
    message=".*deprecated.*Pydantic.*",
    category=UserWarning,
    module="pydantic"
)
warnings.filterwarnings(
    "ignore",
    message=".*path_separator.*Alembic.*",
    category=DeprecationWarning,
    module="alembic"
)


# ---------- 保證 BaseTool 存在 ----------
try:
    from crewai_tools import BaseTool
except ImportError:
    from pydantic import BaseModel
    class BaseTool(BaseModel):
        name: str = "custom-tool"
        description: str = "A user-defined CrewAI tool"
        def run(self, *args, **kwargs):
            return self._run(*args, **kwargs)
        def _run(self, *args, **kwargs):
            raise NotImplementedError


# ---------- 後備 GoogleTrendsTool ----------
try:
    from crewai_tools import GoogleTrendsTool
except ImportError:
    from pytrends.request import TrendReq
    class GoogleTrendsTool(BaseTool):
        name: str = "google-trends"
        description: str = "Google Trends avg score (0–100) last 7d, US"
        def __init__(self, geo="US"):
            super().__init__()
            self.geo = geo
            self._tr = TrendReq(hl="en-US", tz=0)
        def _run(self, keywords: str) -> int:
            kw_list = [k.strip() for k in re.split(r"[,+]", keywords) if k.strip()]
            score = 0
            for kw in kw_list:
                try:
                    self._tr.build_payload([kw], timeframe="now 7-d", geo=self.geo)
                    df = self._tr.interest_over_time()
                    if not df.empty:
                        score = max(score, int(df[kw].mean()))
                except Exception:
                    continue
            return score

TOOL_REGISTRY = {
    "SerperDevTool": SerperDevTool,
    "WebsiteSearchTool": WebsiteSearchTool,
    "GoogleTrendsTool": GoogleTrendsTool  
}

# ---------- CLI ----------
parser = argparse.ArgumentParser()
parser.add_argument(
    "--topic",
    help="研究主題；如果省略則先跑 Trend Scout 並以 Top‑1 熱點為主題"
)
args = parser.parse_args()
skip_trend = bool(args.topic)               # 只看 topic 是否存在


# 2) 建立 ArtifactLogger（放在解析參數之後）
logger = ArtifactLogger()                         # NEW
# 先寫入 inputs
logger.save_inputs({"topic": args.topic or "", "skip_trend": skip_trend})   # NEW
logger.save_env()                                 # NEW


# ---------- ENV ----------
load_dotenv()
assert os.getenv("OPENAI_API_KEY"), "請在環境或 .env 設定 OPENAI_API_KEY"
# Serper API Key（若未用可不填）
if "SerperDevTool" in TOOL_REGISTRY and not os.getenv("SERPER_API_KEY"):
    print("[INFO] SERPER_API_KEY 未設定，Trend Scout / Research 仍可執行但無即時搜尋結果。")

# ---------- YAML 讀檔 ----------
def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

agents_config = load_yaml("agents.yaml")
tasks_config = load_yaml("tasks.yaml")

# 4) 把 YAML 副本存進本次 run 資料夾           # NEW
shutil.copy("agents.yaml", logger.run_dir)
shutil.copy("tasks.yaml", logger.run_dir)


# ---------- 建立 Agents ----------
agents = {}
for name, cfg in agents_config.items():
    # 動態掛工具
    tool_instances = []
    for tool_name in cfg.get("tools", []):
        tool_cls = TOOL_REGISTRY.get(tool_name)
        if tool_cls:
            try:
                tool_instances.append(tool_cls())
            except Exception as e:
                print(f"[WARNING] 無法初始化工具 {tool_name}: {e}")
    agents[name] = Agent(
        name=name,
        role=cfg["role"],
        goal=cfg["goal"],
        backstory=cfg["backstory"],
        tools=tool_instances,
        verbose=cfg.get("verbose", False),
        allow_delegation=cfg.get("allow_delegation", False),
    )

# ---------- 建立 Task 物件（第一輪：不處理 context） ----------
task_map = {}
for tname, cfg in tasks_config.items():
    if skip_trend and tname == "generate_topics":
        continue

    agent = agents[cfg["agent"]]
    desc = cfg["description"].replace("{topic}", args.topic or "")
    exp  = cfg["expected_output"].replace("{topic}", args.topic or "")
    task = Task(
        name=tname,
        agent=agent,
        description=textwrap.dedent(desc),
        expected_output=textwrap.dedent(exp),
        markdown=True,                       # CrewAI 0.14.x 支援
        output_file=cfg.get("output_file"),  # 直接綁定文件名
    )
    task_map[tname] = task

# ---------- 第二輪：補 context 參照 ----------
for tname, cfg in tasks_config.items():
    if tname not in task_map:
        continue
    ctx_names = cfg.get("context", [])
    # 若跳過 trend，且 research_topic 依賴 generate_topics，需清空
    if skip_trend and tname == "research_topic":
        task_map[tname].context = []
        continue
    if ctx_names:
        task_map[tname].context = [
            task_map[n] for n in ctx_names if n in task_map
        ]

# ---------- 組 Crew ----------
crew_tasks = list(task_map.values())
crew = Crew(agents=list(agents.values()), tasks=crew_tasks, verbose=True)

# ---------- 執行 ----------
inputs = {
    "topic": args.topic or "" # 若 CLI 沒給，先傳空字串；Trend Scout 會補
    }
results = crew.kickoff(inputs=inputs)

# ---------- 寫檔工具函式 ----------
def save_output(task_name: str, content: str) -> None:
    fname = tasks_config[task_name].get("output_file")
    if not fname:
        return
    # 在檔尾加 timestamp 以免覆蓋 (可按需關閉)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base, ext = os.path.splitext(fname)
    fname_ts = f"{base}_{timestamp}{ext}"
    with open(fname_ts, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[✓] {task_name} ➜ {fname_ts}")

# ---------- 解析 CrewOutput ----------
if hasattr(results, "to_dict"):
    outputs = results.to_dict()
elif hasattr(results, "outputs"):
    outputs = results.outputs
elif isinstance(results, dict):
    outputs = results
else:
    outputs = {}
    print("[WARNING] 無法解析 CrewOutput 結構。")

for t_name, t_result in outputs.items():
    save_output(t_name, str(t_result))

# ---------- 寫入每個 Task 輸出 ----------
def _to_result_dict(r):
    if isinstance(r, dict):
        return r
    if hasattr(r, "to_dict"):          # CrewOutput ≥0.30
        return r.to_dict()
    # CrewOutput <0.30 → 可迭代 TaskResult
    if hasattr(r, "__iter__"):
        return {t.name: t.output for t in r}
    return {}

result_dict = _to_result_dict(results)

for task_name, content in result_dict.items():
    logger.save_task(task_name, content)

# 7) （可選）明確列印 run_id 供查詢
print(f"\n✅  Run finished. Artifacts saved to: runs/{logger.run_id}\n")
print("\n🎉 Pipeline finished — generated markdown files are ready!")
