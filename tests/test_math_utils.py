import pytest
import utils.math_utils as mu
import requests
from unittest.mock import patch
from pytest_mock import mocker

def test_calculate_mean():
    assert mu.calculate_mean([1, 2, 3]) == 2.0

def test_create_dataframe():
    df = mu.create_dataframe()
    assert 'score' in df.columns
    assert len(df) == 3

def test_generate_range():
    assert mu.generate_range(3) == [0, 1, 4]

def test_exception_handling_demo():
    assert "Caught an error" in mu.exception_handling_demo()

def test_fetch_website_title(mocker):
    mocker.patch.object(requests, 'get')
    requests.get.return_value.text = "<html><head><title>Example</title></head></html>"
    assert mu.fetch_website_title("any") == "Example"