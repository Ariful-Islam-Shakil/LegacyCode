import pytest
import utils.math_utils as mu
import requests

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], 2.0),
])
def test_calculate_mean(numbers, expected):
    assert mu.calculate_mean(numbers) == expected

@pytest.fixture
def dataframe():
    return mu.create_dataframe()

def test_create_dataframe(dataframe):
    assert 'score' in dataframe.columns
    assert len(dataframe) == 3

@pytest.mark.parametrize("n, expected", [
    (3, [0, 1, 4]),
])
def test_generate_range(n, expected):
    assert mu.generate_range(n) == expected

def test_exception_handling_demo():
    assert "Caught an error" in mu.exception_handling_demo()

@pytest.fixture
def mock_response():
    return requests.Response()
    mock_response._content = "<html><head><title>Example</title></head></html>".encode()

@pytest.fixture
def monkeypatched_get(monkeypatch):
    def mock_get(url):
        return mock_response()
    monkeypatch.setattr(requests.api, "requests", lambda *args, **kwargs: mock_response())
    monkeypatch.setattr(requests, "get", mock_get)

def test_fetch_website_title(monkeypatched_get):
    assert mu.fetch_website_title("any") == "Example"