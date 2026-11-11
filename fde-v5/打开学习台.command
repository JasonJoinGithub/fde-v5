#!/bin/bash
# 双击打开 FDE 学习台（macOS）
# 实际工作在 start.sh 里：起本地服务 http://127.0.0.1:8000 再打开浏览器，
# 这样进度才能存住。直接双击 FDE学习App.html 会丢进度，别用那个办法。
cd "$(dirname "$0")" || exit 1
exec ./start.sh
