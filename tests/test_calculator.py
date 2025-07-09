```python
# tests/test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide, display_results_as_table, main

def test_add():
    assert add(5, 3) == 8
    assert add(-5, 3) == -2
    assert add(-5, -3) == -8

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, 3) == -8
    assert subtract(-5, -3) == -2

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(-5, 3) == -15
    assert multiply(-5, -3) == 15

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(-10, -2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_add_invalid_input():
    with pytest.raises(TypeError):
        add("a", 3)

def test_subtract_invalid_input():
    with pytest.raises(TypeError):
        subtract("a", 3)

def test_multiply_invalid_input():
    with pytest.raises(TypeError):
        multiply("a", 3)

def test_divide_invalid_input():
    with pytest.raises(TypeError):
        divide("a", 3)

def test_display_results_as_table():
    with pytest.raises(TypeError):
        display_results_as_table("a", 3)

def test_main():
    with pytest.raises(ValueError):
        main()

def test_main_valid_input():
    with pytest.raises(SystemExit):
        main()

def test_main_invalid_input():
    with pytest.raises(SystemExit):
        main()
```