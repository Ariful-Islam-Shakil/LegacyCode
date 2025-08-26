import pytest
import utils.math_utils as mu
from unittest.mock import patch
import requests

def test_calculate_mean() -> None:
    """
    Test calculate_mean function returns the correct mean.
    """
    assert mu.calculate_mean([1, 2, 3]) == 2.0

def test_create_dataframe() -> None:
    """
    Test create_dataframe function returns a dataframe with 'score' column and 3 rows.
    """
    df = mu.create_dataframe()
    assert 'score' in df.columns
    assert len(df) == 3

def test_generate_range() -> None:
    """
    Test generate_range function returns the correct range.
    """
    assert mu.generate_range(3) == [0, 1, 4]

def test_exception_handling_demo() -> None:
    """
    Test exception_handling_demo function returns the correct error message.
    """
    assert "Caught an error" in mu.exception_handling_demo()

@pytest.mark.parametrize("url, expected_title", [
    ("any", "Example")
])
@patch('utils.math_utils.requests.get')
def test_fetch_website_title(mock_get, url: str, expected_title: str) -> None:
    """
    Test fetch_website_title function returns the correct website title.

    Args:
    - url (str): The URL to fetch.
    - expected_title (str): The expected title.

    """
    mock_response = type('MockResponse', (), {'text': "<html><head><title>Example</title></head></html>"})
    mock_get.return_value = mock_response
    assert mu.fetch_website_title(url) == expected_title