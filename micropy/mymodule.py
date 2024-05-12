"""
Miscellaneous methods that help in <<blah blah>>
Does not require explicit instantiation.

The following actions can be performed:
===============   ===============
Action            Method
===============   ===============
Get a             :meth:`methoda`
Get b             :meth:`methodb`
"""


def say_hello():
    """Test function"""
    # flake8: noqa
    print("Hello")
    return False


def methoda():
    """Gets A ..."""
    return "a"


def methodb():
    """Gets B ..."""
    return "b"


def is_less_than_five(inp):
    """This does this"""
    if inp < 5:
        return True
    return False
