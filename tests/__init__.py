import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
from your_module import your_function

@pytest.mark.parametrize("input_value, expected_output", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_your_function(input_value, expected_output):
    with patch('your_module.your_function') as mock_function:
        mock_function.return_value = expected_output
        result = your_function(input_value)
        assert result == expected_output

def test_your_function_invalid_input():
    with pytest.raises(ValueError):
        your_function("invalid")

def test_your_function_edge_case():
    result = your_function(0)
    assert result == 0

def test_your_function_edge_case_zero_division():
    with pytest.raises(ZeroDivisionError):
        your_function(0, 0)

def test_your_function_edge_case_zero_division_with_context():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        your_function(0, 0, context="division by zero")

def test_your_function_edge_case_zero_division_with_context_and_message():
    with pytest.raises(ZeroDivisionError, match="division by zero: message"):
        your_function(0, 0, context="division by zero", message="message")

def test_your_function_edge_case_zero_division_with_context_and_message_and_custom_exception():
    with pytest.raises(MyCustomException, match="division by zero: message"):
        your_function(0, 0, context="division by zero", message="message")

class MyCustomException(Exception):
    pass