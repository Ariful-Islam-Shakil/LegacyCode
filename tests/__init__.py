# test_example.py
import pytest
from example import example_function

@pytest.mark.parametrize("input_value, expected_output", [
    (1, 2),
    (2, 3),
    (3, 4),
])
def test_example_function(input_value, expected_output):
    assert example_function(input_value) == expected_output

def test_example_function_invalid_input():
    with pytest.raises(ValueError):
        example_function("invalid")

def test_example_function_empty_input():
    with pytest.raises(ValueError):
        example_function("")