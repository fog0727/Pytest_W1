"""
定义类
创建测试方法test开头
创建setup teardown
运行查看结果
"""


#类级别方法 一次测试内只运用一次
#定义类
class TestClass:
#创建setup teardown
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")
    def test_a(self):
        print("test_a")
    def test_b(self):
        print("test_b")
"""pytest_class.py setup_class
test_a
.test_b
.teardown_class
"""