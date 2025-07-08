import pytest
from unittest.mock import patch
from your_module import your_function

@pytest.mark.parametrize("input_value, expected_output", [
    (1, 2),
    (2, 3),
    (3, 4),
])
def test_your_function(input_value, expected_output):
    with patch.object(your_function, 'your_helper_function') as mock_helper:
        mock_helper.return_value = expected_output
        result = your_function(input_value)
        assert result == expected_output

def test_your_function_invalid_input():
    with pytest.raises(ValueError):
        your_function('invalid_input')

def test_your_function_edge_case():
    result = your_function(0)
    assert result == 1

# Refactored test file for Python 3.12

import pytest
from your_module import your_function

@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (1, 2),
        (2, 3),
        (3, 4),
    ],
    ids=["test_1", "test_2", "test_3"],
)
def test_your_function(input_value: int, expected_output: int) -> None:
    with patch.object(your_function, "your_helper_function") as mock_helper:
        mock_helper.return_value = expected_output
        result = your_function(input_value)
        assert result == expected_output

def test_your_function_invalid_input() -> None:
    with pytest.raises(ValueError):
        your_function("invalid_input")

def test_your_function_edge_case() -> None:
    result = your_function(0)
    assert result == 1

# Refactored test file for Python 3.12 with type hints

import pytest
from your_module import your_function

@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (1, 2),
        (2, 3),
        (3, 4),
    ],
    ids=["test_1", "test_2", "test_3"],
)
def test_your_function(input_value: int, expected_output: int) -> None:
    with patch.object(your_function, "your_helper_function") as mock_helper:
        mock_helper.return_value = expected_output
        result = your_function(input_value)
        assert result == expected_output

def test_your_function_invalid_input() -> None:
    with pytest.raises(ValueError):
        your_function("invalid_input")

def test_your_function_edge_case() -> None:
    result = your_function(0)
    assert result == 1