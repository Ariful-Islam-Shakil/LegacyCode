from collections import Counter
from io import StringIO
from typing import List, Dict, Tuple

def say_hello(name: str) -> str:
    """Returns a personalized greeting message.

    Args:
        name (str): The name to be included in the greeting.

    Returns:
        str: A greeting message with the provided name.
    """
    return f"Hello, {name}!"

def count_words(text: str) -> Counter:
    """Counts the occurrences of each word in the provided text.

    Args:
        text (str): The text to be analyzed.

    Returns:
        Counter: A dictionary-like object containing word frequencies.
    """
    words = text.lower().split()
    return Counter(words)

def string_io_example() -> str:
    """Demonstrates the use of StringIO for string buffering.

    Returns:
        str: The contents of the string buffer.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.x with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration(d: Dict[str, int]) -> List[str]:
    """Iterates over a dictionary and returns a list of key-value pairs.

    Args:
        d (Dict[str, int]): The dictionary to be iterated.

    Returns:
        List[str]: A list of string representations of key-value pairs.
    """
    result = []
    for k, v in d.items():
        result.append(f"{k} => {v}")
    return result