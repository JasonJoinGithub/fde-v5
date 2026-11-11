#!/bin/bash
# 打开 FDE 学习台（macOS / Linux）
#
# 为什么不用直接双击 FDE学习App.html：
#   浏览器把 file:// 打开的页面当成不可靠的来源。Safari 在这种打开方式下
#   存不住 localStorage；Chrome 则按文件路径给每个副本各存一份进度——
#   打开 v3 的副本、v4 的副本、重新下载的副本，进度各算各的，等于每次从零开始。
#   这就是以前每次打开都重新开始的根因。
#   这个脚本改成起一个本地服务：http://127.0.0.1:8000 是一个固定来源（origin），
#   不管 HTML 是哪个版本，只要从同一个服务打开，进度（localStorage，key 仍是
#   fde_app_v1）都存在同一个地方，跨版本也能留住。
#   服务只在你自己电脑上跑，不联网、不上传任何东西。
# 停止：回到这个终端窗口，按 Ctrl+C。

cd "$(dirname "$0")" || exit 1
PORT=8000
URL="http://127.0.0.1:$PORT/FDE学习App.html"

# 先清掉占着 8000 端口的旧服务（如果有）
if command -v lsof >/dev/null 2>&1; then
  OLD_PIDS=$(lsof -ti :"$PORT" 2>/dev/null || true)
  if [ -n "$OLD_PIDS" ]; then
    echo "端口 $PORT 已被占用，先停掉旧服务：$OLD_PIDS"
    echo "$OLD_PIDS" | xargs kill 2>/dev/null || true
    sleep 1
  fi
fi

# 起本地服务（后台跑，日志写 /tmp/fde-server.log）
python3 -m http.server "$PORT" >/tmp/fde-server.log 2>&1 &
SERVER_PID=$!
trap 'kill $SERVER_PID 2>/dev/null; exit 0' INT TERM EXIT

# 等服务起来（最多等 6 秒）
OK=0
for _ in $(seq 1 20); do
  if command -v curl >/dev/null 2>&1; then
    curl -s -o /dev/null "$URL" && OK=1 && break
  else
    sleep 1; OK=1; break
  fi
  sleep 0.3
done
if [ "$OK" != "1" ]; then
  echo "本地服务没起来，请看日志：/tmp/fde-server.log"
  exit 1
fi

echo "学习台已启动：$URL"
echo "进度存在这个地址的浏览器里，关掉页面也不会丢；按 Ctrl+C 停止服务。"

# 打开浏览器
if command -v open >/dev/null 2>&1; then
  open "$URL"
elif command -v xdg-open >/dev/null 2>&1; then
  xdg-open "$URL"
else
  echo "请手动打开：$URL"
fi

# 前台等着服务跑；Ctrl+C 时 trap 会停掉它
wait $SERVER_PID
