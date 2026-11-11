import os
import sys
import tempfile
import unittest

# 把 week2 目录加入模块搜索路径，这样从 fde-code 目录运行也能导入 batch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from batch import analyze_one


def make_file(content):
    """造一个临时文件，返回路径。调用方负责删除。"""
    fd, path = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(content)
    return path


class AnalyzeOneTest(unittest.TestCase):
    """测试 batch.py 里的 analyze_one。"""

    def test_normal_file(self):
        """普通文件：两行非空文本。"""
        path = make_file("第一行\n第二行\n")
        try:
            result = analyze_one(path)
            self.assertEqual(result["total"], 2)
            self.assertEqual(result["empty"], 0)
        finally:
            os.remove(path)

    def test_empty_lines(self):
        """包含空白行的文件：4 行里有 2 行是空白行。"""
        path = make_file("第一行\n\n\n第四行\n")
        try:
            result = analyze_one(path)
            self.assertEqual(result["total"], 4)
            self.assertEqual(result["empty"], 2)
        finally:
            os.remove(path)

    def test_empty_file(self):
        """空文件：0 行，0 个空白行。"""
        path = make_file("")
        try:
            result = analyze_one(path)
            self.assertEqual(result["total"], 0)
            self.assertEqual(result["empty"], 0)
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main()
