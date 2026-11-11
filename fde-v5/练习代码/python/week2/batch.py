import os
import sys


def analyze_one(path):
    """读取一个文本文件，返回总行数和空白行数。"""
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total = len(lines)
    empty = 0
    for line in lines:
        if line.strip() == "":
            empty = empty + 1

    return {"path": path, "total": total, "empty": empty}


def main():
    # 检查有没有传入文件夹路径
    if len(sys.argv) < 2:
        print("用法：python3 batch.py 文件夹路径")
        return

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print("文件夹不存在：" + folder)
        return

    # 排序后再遍历，保证每次输出顺序一样
    names = sorted(os.listdir(folder))

    file_count = 0
    all_lines = 0

    for name in names:
        # 只处理 .txt 文件
        if not name.endswith(".txt"):
            continue

        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue

        info = analyze_one(path)
        print("文件：" + info["path"])
        print("  总行数：" + str(info["total"]))
        print("  空白行数：" + str(info["empty"]))

        file_count = file_count + 1
        all_lines = all_lines + info["total"]

    print("----------")
    print("文件总数：" + str(file_count))
    print("总行数：" + str(all_lines))


if __name__ == "__main__":
    main()
