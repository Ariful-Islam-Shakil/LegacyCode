```python
# tests/test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide, display_results_as_table

def test_add():
    assert add(5, 3) == 8
    assert add(-5, 3) == -2
    assert add(-5, -3) == -8

def test_add_invalid_input():
    with pytest.raises(TypeError):
        add("five", 3)
    with pytest.raises(TypeError):
        add(5, "three")

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, 3) == -8
    assert subtract(-5, -3) == -2

def test_subtract_invalid_input():
    with pytest.raises(TypeError):
        subtract("five", 3)
    with pytest.raises(TypeError):
        subtract(5, "three")

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(-5, 3) == -15
    assert multiply(-5, -3) == 15

def test_multiply_invalid_input():
    with pytest.raises(TypeError):
        multiply("five", 3)
    with pytest.raises(TypeError):
        multiply(5, "three")

def test_divide():
    assert divide(5, 3) == 1.6666666666666667
    assert divide(-5, 3) == -1.6666666666666667
    assert divide(-5, -3) == 1.6666666666666667

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_divide_invalid_input():
    with pytest.raises(TypeError):
        divide("five", 3)
    with pytest.raises(TypeError):
        divide(5, "three")

def test_display_results_as_table():
    with pytest.raises(ValueError):
        display_results_as_table(5, 0)
    display_results_as_table(5, 3)
    display_results_as_table(-5, 3)
    display_results_as_table(-5, -3)

def test_main():
    with pytest.raises(ValueError):
        main()
```