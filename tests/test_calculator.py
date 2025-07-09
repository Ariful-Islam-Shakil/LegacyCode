
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

def test_add_type_error():
    with pytest.raises(TypeError):
        add("5", 3)

def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract("5", 3)

def test_multiply_type_error():
    with pytest.raises(TypeError):
        multiply("5", 3)

def test_divide_type_error():
    with pytest.raises(TypeError):
        divide("5", 3)

def test_display_results_as_table():
    results = [
        ["Operation", "Result"],
        ["Addition", 13],
        ["Subtraction", 7],
        ["Multiplication", 65],
        ["Division", 2.6]
    ]
    with pytest.raises(SystemExit):
        display_results_as_table(10, 3)

def test_main():
    with pytest.raises(SystemExit):
        main()
