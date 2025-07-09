import pytest
from unittest.mock import patch
from your_module import your_function

@pytest.mark.parametrize("input_value, expected_output", [
    (1, 2),
    (2, 3),
    (3, 4),
])
def test_your_function(input_value, expected_output):
    with patch.object(your_function, 'your_dependency') as mock_dependency:
        mock_dependency.return_value = 1
        result = your_function(input_value)
        assert result == expected_output

def test_your_function_invalid_input():
    with pytest.raises(ValueError):
        your_function('invalid')

def test_your_function_edge_case():
    result = your_function(0)
    assert result == 1

def test_your_function_edge_case_zero():
    result = your_function(0)
    assert result == 1

def test_your_function_edge_case_negative():
    with pytest.raises(ValueError):
        your_function(-1)

def test_your_function_edge_case_float():
    result = your_function(0.5)
    assert result == 1

# your_module.py
def your_function(input_value):
    if not isinstance(input_value, int):
        raise ValueError("Input must be an integer")
    if input_value < 0:
        raise ValueError("Input must be a non-negative integer")
    if input_value == 0:
        return 1
    return input_value + 1

# requirements.txt
pytest==7.1.2