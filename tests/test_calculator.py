```python
# tests/test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide, display_results_as_table, main

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
    with pytest.raises(ValueError):
        display_results_as_table(5, 0)
    display_results_as_table(5, 3)

def test_main():
    capturedOutput = pytest.raises(ValueError)
    main()
    assert "Error: Cannot divide by zero!" in str(capturedOutput.value)

def test_main_no_error():
    capturedOutput = pytest.capsys
    with pytest.raises(SystemExit):
        main()
    assert "Performing calculations on 10 and 5" in capturedOutput.out
    assert "Error: Cannot divide by zero!" not in capturedOutput.out
```