import pytest

from myapp.mymodule.funcs import *

@pytest.mark.ut
def test_add():
    # This test will fail
    assert add(4, 8) == 13

@pytest.mark.it
def test_add_subtract():
    # This test will fail
    assert subtract(add(4, 8), 6) == 7

@pytest.mark.it
def test_multiply():
    # This test will success. 
    assert multiply(divide(56, 8), 5) == 35

@pytest.mark.ut
def test_divide():
    assert divide(56, 8) == 7
