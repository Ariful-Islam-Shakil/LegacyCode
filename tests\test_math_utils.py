import pytest
import utils.math_utils as mu
import requests

def test_calculate_mean():
    """
    Test calculate_mean function.

    Args:
        None

    Returns:
        None
    """
    assert mu.calculate_mean([1, 2, 3]) == 2.0


def test_create_dataframe():
    """
    Test create_dataframe function.

    Args:
        None

    Returns:
        None
    """
    df = mu.create_dataframe()
    assert 'score' in df.columns
    assert len(df) == 3


def test_generate_range():
    """
    Test generate_range function.

    Args:
        None

    Returns:
        None
    """
    assert mu.generate_range(3) == [0, 1, 4]


def test_exception_handling_demo():
    """
    Test exception_handling_demo function.

    Args:
        None

    Returns:
        None
    """
    assert "Caught an error" in mu.exception_handling_demo()


@pytest.mark.parametrize("url, expected_title", [
    ("any", "Example")
])
def test_fetch_website_title(monkeypatch, url, expected_title):
    """
    Test fetch_website_title function.

    Args:
        monkeypatch: pytest fixture
        url (str): URL to fetch
        expected_title (str): Expected title

    Returns:
        None
    """
    class MockResponse:
        text = "<html><head><title>Example</title></head></html>"

    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    assert mu.fetch_website_title(url) == expected_title