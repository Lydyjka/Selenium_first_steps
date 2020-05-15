import pytest

@pytest.mark.skip
def test_method():
    x = 5
    y = 2
    assert x + y == 7, "Assertion failed, Expected 7"
    assert x + y == 2, "Assertion failed, Expected 2"

def test_method2():
    x = 5
    y = 2
    assert x + y == 7, "Assertion failed, Expected 7"
    assert x + y == 7, "Assertion failed, Expected 7"

@pytest.mark.xfail
def test_method3():
    x = 5
    y = 2
    assert x + y == 7, "Assertion failed, Expected 7"
    assert x + y == 2, "Assertion failed, Expected 2"