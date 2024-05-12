"""Sample test file"""
from .mymodule import is_less_than_five, methoda, methodb, say_hello


def test_hello():
    """Tests sayHello function"""
    assert say_hello() is False


def test_a():
    """Tests methoda function"""
    assert methoda() == "a"
    assert methodb() == "b"

    assert is_less_than_five(4) is True
    assert is_less_than_five(6) is False
