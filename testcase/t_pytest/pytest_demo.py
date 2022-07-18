import pytest


def func(x):
    return x+1
#失败重试  同pytest.ini
@pytest.mark.flaky(reruns=5,reruns_delay=2)
def test_a():
    print("test_a1111111111")
    assert func(3) == 5
def test_c():
    print("test_c1111111111")
    assert func(3) == 5
#失败重试  同pytest.ini
# @pytest.mark.flaky(reruns=5,reruns_delay=2)
def test_b():
    print("test_b1111111111")
    assert 1

if __name__ == "__main__":
    pytest.main(["pytest_demo.py"])