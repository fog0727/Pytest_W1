"""
定义类
创建测试方法test开头
创建setup teardown
运行查看结果
"""


#函数级别方法 运行一次函数内运用一次
#定义类
class TestFunc:
#创建setup teardown
    def setup(self):
        print("setup---开头")
    def teardown(self):
        print("teardown-----结尾")

#创建测试方法test开头
    def test_a(self):
        print("test_a")
    def test_b(self):
        print("test_b")
"""pytest_func.py setup---开头
test_a
.teardown-----结尾
setup---开头
test_b
.teardown-----结尾
"""