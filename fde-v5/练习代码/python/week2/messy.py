# 用法：python3 messy.py 文件名.txt
# 这个文件故意写成一整段，请把下面的流程拆成 3 个函数。

import os
import sys

if len(sys.argv) < 2 or os.path.isfile(sys.argv[1]) == False:
    print("用法：python3 messy.py 文件名.txt")
    sys.exit(1)

file_path = sys.argv[1]

file = open(file_path, "r", encoding="utf-8")
lines = file.readlines()
file.close()

total = 0
empty = 0
word_count = 0
longest_chars = 0
longest_content = ""

for line in lines:
    total = total + 1
    text = line.strip()
    if text == "":
        empty = empty + 1
    word_count = word_count + len(text.split())
    if len(text) > longest_chars:
        longest_chars = len(text)
        longest_content = text

print("文件：" + file_path)
print("总行数：" + str(total))
print("空行数：" + str(empty))
print("词数：" + str(word_count))
print("最长行字数：" + str(longest_chars))
print("最长行内容：" + longest_content)
print("========== 统计结束 ==========")
# 提示：可以按“读取文件、统计、输出”三步来拆分。
