#!/bin/bash
# 授权后，跑这个脚本就会创建仓库并推送
set -e
REPO_NAME="${1:-fde-learning-app}"
cd "$(dirname "$0")"

echo "==> 检查登录状态"
gh auth status || { echo "请先运行：gh auth login -h github.com -w"; exit 1; }

echo "==> 创建仓库 $REPO_NAME（如果已存在就跳过）"
if gh repo view "$USER/$REPO_NAME" >/dev/null 2>&1; then
  echo "仓库已存在，直接推送"
else
  gh repo create "$REPO_NAME" --public --source=. --remote=origin --push \
    --description "FDE 学习台：12 周从零到能面试（离线单文件 App + 教程 + 练习代码）"
  echo "==> 已创建并推送"
  exit 0
fi

git remote get-url origin >/dev/null 2>&1 || gh repo set-default "$USER/$REPO_NAME"
git push -u origin main
echo "==> 推送完成"
