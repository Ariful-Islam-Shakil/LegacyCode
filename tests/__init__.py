import pytest
from unittest.mock import patch
from your_module import your_function

@pytest.mark.parametrize("input_value, expected_output", [
    (1, 2),
    (2, 3),
    (3, 4),
])
def test_your_function(input_value, expected_output):
    with patch('builtins.print') as mock_print:
        result = your_function(input_value)
        assert result == expected_output
        mock_print.assert_not_called()

def test_your_function_invalid_input():
    with pytest.raises(TypeError):
        your_function("invalid_input")

def test_your_function_edge_case():
    with pytest.raises(ZeroDivisionError):
        your_function(0)

def test_your_function_edge_case_2():
    with pytest.raises(ZeroDivisionError):
        your_function(-1)

def test_your_function_edge_case_3():
    with pytest.raises(ZeroDivisionError):
        your_function(-2)

def test_your_function_edge_case_4():
    with pytest.raises(ZeroDivisionError):
        your_function(-3)

def test_your_function_edge_case_5():
    with pytest.raises(ZeroDivisionError):
        your_function(-4)

def test_your_function_edge_case_6():
    with pytest.raises(ZeroDivisionError):
        your_function(-5)