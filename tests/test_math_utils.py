import pytest
from unittest.mock import patch
import utils.math_utils as mu

@pytest.mark.parametrize("numbers, expected_mean", [
    ([1, 2, 3], 2.0),
    ([4, 5, 6], 5.0),
    ([7, 8, 9], 8.0)
])
def test_calculate_mean(numbers, expected_mean):
    assert mu.calculate_mean(numbers) == expected_mean

def test_create_dataframe():
    df = mu.create_dataframe()
    assert 'score' in df.columns
    assert len(df) == 3

def test_generate_range():
    assert mu.generate_range(3) == [0, 1, 4]

def test_exception_handling_demo():
    assert "Caught an error" in mu.exception_handling_demo()

@pytest.mark.asyncio
async def test_fetch_website_title(monkeypatch):
    class MockResponse:
        text = "<html><head><title>Example</title></head></html>"
    @patch('utils.math_utils.requests.get')
    def mock_get(get):
        return MockResponse()
    monkeypatch.setattr(mu, "requests", mock_get)
    assert mu.fetch_website_title("any") == "Example"