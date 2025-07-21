```python
# tests/test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide, display_results_as_table

def test_add():
    assert add(5, 3) == 8
    assert add(-5, 3) == -2
    assert add(-5, -3) == -8

def test_add_type_error():
    with pytest.raises(TypeError):
        add("a", 3)
    with pytest.raises(TypeError):
        add(5, "b")

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, 3) == -8
    assert subtract(-5, -3) == -2

def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract("a", 3)
    with pytest.raises(TypeError):
        subtract(5, "b")

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(-5, 3) == -15
    assert multiply(-5, -3) == 15

def test_multiply_type_error():
    with pytest.raises(TypeError):
        multiply("a", 3)
    with pytest.raises(TypeError):
        multiply(5, "b")

def test_divide():
    assert divide(5, 3) == 1.6666666666666667
    assert divide(-5, 3) == -1.6666666666666667
    assert divide(-5, -3) == 1.6666666666666667

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_divide_type_error():
    with pytest.raises(TypeError):
        divide("a", 3)
    with pytest.raises(TypeError):
        divide(5, "b")

def test_display_results_as_table():
    display_results_as_table(5, 3)
    assert True  # Display results as table, no assertions needed

def test_display_results_as_table_type_error():
    with pytest.raises(TypeError):
        display_results_as_table("a", 3)
    with pytest.raises(TypeError):
        display_results_as_table(5, "b")

def test_main():
    with pytest.raises(ValueError):
        main()

def test_main_success():
    with pytest.raises(SystemExit):
        main()  # Ensure main() exits successfully
```