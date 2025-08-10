import pytest
from main import *

def test_func():
    assert func("Hello") == "String"
    assert func(123) == "Integer"
    assert func(123.45) == "Float"
    assert func([1, 2, 3]) == "Unknown"
    assert func(None) == "None"                 # Fail 

# We can also use the parameterized tests

@pytest.mark.parametrize("input, expected", [
    ("Hello", "String"),
    (123, "Integer"),
    (123.45, "Float"),
    ([1, 2, 3], "Unknown"),
    (None, "None")                              # Fail
])

def test_func_param(input, expected):
    assert func(input) == expected



def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)