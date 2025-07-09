import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
from your_module import your_function

@pytest.fixture
def mock_open():
    with patch('builtins.open', new_callable=MagicMock) as mock:
        yield mock

def test_your_function(mock_open):
    mock_open.return_value.__enter__.return_value.read.return_value = 'test content'
    result = your_function()
    assert result == 'test content'
    mock_open.assert_called_once_with('path_to_your_file', 'r')

def test_your_function_with_exception(mock_open):
    mock_open.return_value.__enter__.return_value.read.side_effect = Exception('test exception')
    with pytest.raises(Exception):
        your_function()
    mock_open.assert_called_once_with('path_to_your_file', 'r')

def test_your_function_with_file_not_found(mock_open):
    mock_open.return_value.__enter__.return_value.read.return_value = None
    with pytest.raises(FileNotFoundError):
        your_function()
    mock_open.assert_called_once_with('path_to_your_file', 'r')

# your_module.py
def your_function():
    with open('path_to_your_file', 'r') as file:
        return file.read()

# conftest.py
import pytest
from _pytest.config import Config
from _pytest.nodes import Item

@pytest.hookimpl
def pytest_configure(config: Config) -> None:
    config.addinivalue_line(
        "markers",
        "slow: mark tests as slow (t>2sec)"
    )