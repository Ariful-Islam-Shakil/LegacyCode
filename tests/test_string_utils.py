import pytest
import utils.string_utils as su
from typing import Dict

def test_say_hello_name() -> None:
    """Test say_hello function with a name"""
    assert su.say_hello("Alice") == "Hello, Alice!"

def test_count_words_in_string() -> None:
    """Test count_words function with a string"""
    result: Dict[str, int] = su.count_words("Hello hello world")
    assert result["hello"] == 2
    assert result["world"] == 1

def test_string_io_example_output() -> None:
    """Test string_io_example function"""
    output: str = su.string_io_example()
    assert "string buffer" in output

def test_dictionary_iteration_output() -> None:
    """Test dictionary_iteration function"""
    output: str = su.dictionary_iteration()
    assert "a => 1" in output
    assert "b => 2" in output