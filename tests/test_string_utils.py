import pytest
import utils.string_utils as su
from typing import Dict

def test_say_hello() -> None:
    """
    Test the say_hello function.

    Args:
        None

    Returns:
        None
    """
    assert su.say_hello("Alice") == "Hello, Alice!"

def test_count_words() -> None:
    """
    Test the count_words function.

    Args:
        None

    Returns:
        None
    """
    result: Dict[str, int] = su.count_words("Hello hello world")
    assert result["hello"] == 2
    assert result["world"] == 1

def test_string_io_example() -> None:
    """
    Test the string_io_example function.

    Args:
        None

    Returns:
        None
    """
    output: str = su.string_io_example()
    assert "string buffer" in output

def test_dictionary_iteration() -> None:
    """
    Test the dictionary_iteration function.

    Args:
        None

    Returns:
        None
    """
    output: str = su.dictionary_iteration()
    assert "a => 1" in output
    assert "b => 2" in output