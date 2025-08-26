import pytest
import utils.math_utils as mu
import requests

def test_calculate_mean() -> None:
    """
    Test calculate_mean function returns the correct mean value.

    Args:
        None

    Returns:
        None
    """
    assert mu.calculate_mean([1, 2, 3]) == 2.0

def test_create_dataframe() -> None:
    """
    Test create_dataframe function returns a DataFrame with 'score' column and 3 rows.

    Args:
        None

    Returns:
        None
    """
    df = mu.create_dataframe()
    assert 'score' in df.columns
    assert len(df) == 3

def test_generate_range() -> None:
    """
    Test generate_range function returns the correct range.

    Args:
        None

    Returns:
        None
    """
    assert mu.generate_range(3) == [0, 1, 4]

def test_exception_handling_demo() -> None:
    """
    Test exception_handling_demo function returns the correct error message.

    Args:
        None

    Returns:
        None
    """
    assert "Caught an error" in mu.exception_handling_demo()

@pytest.mark.parametrize("url, expected_title", [
    ("any", "Example"),
])
def test_fetch_website_title(url: str, expected_title: str, monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Test fetch_website_title function returns the correct website title.

    Args:
        url (str): URL to fetch
        expected_title (str): Expected title
        monkeypatch (pytest.MonkeyPatch): Monkey patch object

    Returns:
        None
    """
    class MockResponse:
        text = "<html><head><title>Example</title></head></html>"

    def mock_get(url: str) -> MockResponse:
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    assert mu.fetch_website_title(url) == expected_title