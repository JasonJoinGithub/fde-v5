# week2 练习代码

本目录是 Python 3.9 初学者教程的练习代码。代码使用中文注释，写法尽量朴素。每个文件都可以用 `python3` 启动；`batch.py` 和 `messy.py` 需要传入路径参数。

## 文件说明

- `batch.py`：批量统计一个文件夹里所有 `.txt` 文件的总行数和空白行数。
- `test_analyze.py`：用 Python 自带的 unittest 测试 `batch.py` 里的 `analyze_one` 函数，共 3 个测试。**不需要安装任何东西。**
- `bug1.py`：故意保留除零错误，用来观察报错信息。
- `bug2.py`：故意保留大小写敏感问题，用来观察结果和预期不一致。
- `bug3.py`：故意保留闭包陷阱，用来观察 lambda 晚绑定导致的结果。
- `messy.py`：故意写成没有函数的一整段流程，练习把它重构成 3 个函数。
- `README.md`：本说明文件。

## 运行方法

先进入 week2 目录：

```bash
cd 练习代码/python/week2
```

### batch.py

参数是一个文件夹路径，程序只统计其中的 `.txt` 文件：

```bash
python3 batch.py 你的文件夹路径
```

例如：

```bash
mkdir -p /tmp/week2_txts
printf '第一行\n\n第三行\n' > /tmp/week2_txts/a.txt
printf 'hello world\n' > /tmp/week2_txts/b.txt
python3 batch.py /tmp/week2_txts
```

如果文件夹不存在，程序会打印中文提示，不会崩溃。

### test_analyze.py

用 Python 自带的 `unittest`，**零安装**：

```bash
cd 练习代码/python/week2
python3 -m unittest test_analyze -v
```

也可以从上一级目录跑：

```bash
cd <仓库根目录>
python3 -m unittest week2.test_analyze -v
```

期望看到 3 个 `ok`，最后一行是 `OK`。

想验证"测试真的有用"，把 `batch.py` 里算 `empty` 的那行改成 `empty = 0`，
再跑一次，会看到 `AssertionError` 和 `FAILED`。改回去即可。

### bug1.py、bug2.py、bug3.py

直接运行，观察它们各自的报错或意外输出：

```bash
python3 bug1.py
python3 bug2.py
python3 bug3.py
```

这三个文件是故意保留问题的，不要修改。

### messy.py

参数是一个文本文件路径：

```bash
python3 messy.py 你的文件.txt
```

例如：

```bash
python3 messy.py /tmp/week2_txts/a.txt
```

它会打印总行数、空行数、词数和最长行字数。下一步是把这段顶层流程拆成 3 个函数。
