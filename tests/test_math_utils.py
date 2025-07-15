import pytest
from utils.math_utils import calculate_mean, create_dataframe, generate_range, exception_handling_demo, fetch_website_title
import requests

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], 2.0),
])
def test_calculate_mean(numbers, expected):
    assert calculate_mean(numbers) == expected

def test_create_dataframe():
    df = create_dataframe()
    assert 'score' in df.columns
    assert len(df) == 3

def test_generate_range():
    assert generate_range(3) == [0, 1, 4]

def test_exception_handling_demo():
    assert "Caught an error" in exception_handling_demo()

@pytest.mark.vcr()
def test_fetch_website_title(monkeypatch):
    class MockResponse:
        text = "<html><head><title>Example</title></head></html>"
    def mock_get(url):
        return MockResponse()
    monkeypatch.setattr(requests, "get", mock_get)
    assert fetch_website_title("any") == "Example"