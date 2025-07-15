```python
# tests/test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide, display_results_as_table

def test_add():
    assert add(5, 3) == 8
    assert add(-5, 3) == -2
    assert add(0, 0) == 0

def test_add_type_error():
    with pytest.raises(TypeError):
        add("5", 3)
    with pytest.raises(TypeError):
        add(5, "3")

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, 3) == -8
    assert subtract(0, 0) == 0

def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract("5", 3)
    with pytest.raises(TypeError):
        subtract(5, "3")

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(-5, 3) == -15
    assert multiply(0, 0) == 0

def test_multiply_type_error():
    with pytest.raises(TypeError):
        multiply("5", 3)
    with pytest.raises(TypeError):
        multiply(5, "3")

def test_divide():
    assert divide(5, 3) == 1.6666666666666667
    assert divide(-5, 3) == -1.6666666666666667
    assert divide(0, 0) == 0

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_divide_type_error():
    with pytest.raises(TypeError):
        divide("5", 3)
    with pytest.raises(TypeError):
        divide(5, "3")

def test_display_results_as_table():
    results = [
        ["Operation", "Result"],
        ["Addition", "13"],
        ["Subtraction", "7"],
        ["Multiplication", "65"],
        ["Division", "2.6"]
    ]
    display_results_as_table(8, 5)
    assert results == [
        ["Operation", "Result"],
        ["Addition", "13"],
        ["Subtraction", "7"],
        ["Multiplication", "40"],
        ["Division", "1.6"]
    ]

def test_main():
    with pytest.raises(ValueError):
        main()

def test_main_success(capsys):
    main()
    captured = capsys.readouterr()
    assert "Performing calculations on 10 and 5" in captured.out
    assert "Error: Cannot divide by zero!" in captured.out
```