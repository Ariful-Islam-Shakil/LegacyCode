# test_example.py
import pytest
from example import Example

@pytest.mark.parametrize("input_value, expected_output", [
    (1, True),
    (0, False),
    (-1, False),
])
def test_example(input_value, expected_output):
    example = Example()
    result = example.method(input_value)
    assert result == expected_output

def test_example_invalid_input():
    example = Example()
    with pytest.raises(ValueError):
        example.method("invalid")

def test_example_invalid_input_type():
    example = Example()
    with pytest.raises(TypeError):
        example.method(1.5)

def test_example_invalid_method():
    example = Example()
    with pytest.raises(NotImplementedError):
        example.invalid_method()

# conftest.py
import pytest

@pytest.fixture
def example():
    return Example()

# example.py
class Example:
    def method(self, input_value):
        if not isinstance(input_value, int):
            raise TypeError("Input must be an integer")
        if input_value < 0:
            raise ValueError("Input must be non-negative")
        return input_value > 0

    def invalid_method(self):
        raise NotImplementedError("Method not implemented")

# pytest.ini
[pytest]
python_version = 3.12