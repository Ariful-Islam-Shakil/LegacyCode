import pytest
from utils.string_utils import say_hello, count_words, string_io_example, dictionary_iteration

def test_say_hello():
    assert say_hello("Alice") == "Hello, Alice!"

def test_count_words():
    result = count_words("Hello hello world")
    assert result["hello"] == 2
    assert result["world"] == 1

def test_string_io_example():
    output = string_io_example()
    assert "string buffer" in output

def test_dictionary_iteration():
    output = dictionary_iteration()
    assert "a => 1" in output
    assert "b => 2" in output