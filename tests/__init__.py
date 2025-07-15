# test_example.py
import pytest
from example import example_function

def test_example_function():
    result = example_function(5)
    assert result == 10

def test_example_function_negative_input():
    with pytest.raises(ValueError):
        example_function(-5)

def test_example_function_non_integer_input():
    with pytest.raises(TypeError):
        example_function(5.5)

def test_example_function_zero_input():
    result = example_function(0)
    assert result == 0

# conftest.py
import pytest
from _pytest.config import Config
from _pytest.nodes import ItemCollector

@pytest.fixture
def example_fixture():
    return 5

@pytest.fixture
def example_fixture_negative():
    return -5

@pytest.fixture
def example_fixture_non_integer():
    return 5.5

@pytest.fixture
def example_fixture_zero():
    return 0

# pytest.ini
[pytest]
python_versions = 3.12

# requirements.txt
pytest==7.2.0