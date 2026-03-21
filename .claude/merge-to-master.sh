#!/bin/bash

# Merge current branch to master and push after each session

input=$(cat)

# Recursion prevention
stop_hook_active=$(echo "$input" | jq -r '.stop_hook_active')
if [[ "$stop_hook_active" = "true" ]]; then
  exit 0
fi

# Only run in this repo
repo_root=$(git rev-parse --show-toplevel 2>/dev/null)
if [[ "$repo_root" != *"xhs_content_generator"* ]]; then
  exit 0
fi

current_branch=$(git branch --show-current)

# Nothing to do if already on master
if [[ "$current_branch" = "master" ]]; then
  exit 0
fi

# Must have no uncommitted changes before merging
if ! git diff --quiet || ! git diff --cached --quiet; then
  exit 0
fi

# Merge to master
git checkout master 2>/dev/null
git merge "$current_branch" --ff-only 2>/dev/null

if [[ $? -eq 0 ]]; then
  git push origin master 2>/dev/null
  if [[ $? -eq 0 ]]; then
    echo '{"systemMessage": "✅ Merged '"$current_branch"' → master and pushed."}'
  else
    echo '{"systemMessage": "⚠️ Merged locally but push failed (check branch protection). Run: git push origin master"}'
  fi
fi

# Switch back to original branch
git checkout "$current_branch" 2>/dev/null

exit 0
