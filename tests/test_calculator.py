
# tests/test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide, display_results_as_table

def test_add_positive_numbers():
    result = add(5, 3)
    assert result == 8

def test_add_negative_numbers():
    result = add(-5, -3)
    assert result == -8

def test_add_mixed_numbers():
    result = add(-5, 3)
    assert result == -2

def test_subtract_positive_numbers():
    result = subtract(5, 3)
    assert result == 2

def test_subtract_negative_numbers():
    result = subtract(-5, -3)
    assert result == -2

def test_subtract_mixed_numbers():
    result = subtract(-5, 3)
    assert result == -8

def test_multiply_positive_numbers():
    result = multiply(5, 3)
    assert result == 15

def test_multiply_negative_numbers():
    result = multiply(-5, -3)
    assert result == 15

def test_multiply_mixed_numbers():
    result = multiply(-5, 3)
    assert result == -15

def test_divide_positive_numbers():
    result = divide(10, 2)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_negative_numbers():
    result = divide(-10, 2)
    assert result == -5

def test_divide_mixed_numbers():
    result = divide(-10, 2)
    assert result == -5

def test_display_results_as_table():
    with pytest.raises(ValueError):
        display_results_as_table(10, 0)

def test_display_results_as_table_positive_numbers():
    display_results_as_table(10, 5)

def test_display_results_as_table_negative_numbers():
    display_results_as_table(-10, -5)

def test_display_results_as_table_mixed_numbers():
    display_results_as_table(-10, 5)

def test_add_non_numeric_input():
    with pytest.raises(TypeError):
        add("a", 3)

def test_subtract_non_numeric_input():
    with pytest.raises(TypeError):
        subtract("a", 3)

def test_multiply_non_numeric_input():
    with pytest.raises(TypeError):
        multiply("a", 3)

def test_divide_non_numeric_input():
    with pytest.raises(TypeError):
        divide("a", 3)
