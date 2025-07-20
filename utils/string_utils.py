from io import StringIO
from collections import Counter

def say_hello(name: str) -> str:
    """
    Returns a personalized greeting message.

    Args:
        name (str): The name to be included in the greeting.

    Returns:
        str: A greeting message with the provided name.
    """
    return f"Hello, {name}!"

def count_words(text: str) -> Counter:
    """
    Counts the occurrences of each word in the given text.

    Args:
        text (str): The text to be analyzed.

    Returns:
        Counter: A dictionary-like object containing word frequencies.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input text must be a string")
    words = text.lower().split()
    return Counter(words)

def string_io_example() -> str:
    """
    Demonstrates the usage of StringIO for string buffering.

    Returns:
        str: The contents of the string buffer.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.12 with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration(d: dict[str, int]) -> list[str]:
    """
    Iterates over a dictionary and returns a list of key-value pairs.

    Args:
        d (dict[str, int]): The dictionary to be iterated.

    Returns:
        list[str]: A list of key-value pairs as strings.

    Raises:
        TypeError: If the input is not a dictionary.
    """
    if not isinstance(d, dict):
        raise TypeError("Input must be a dictionary")
    result = [f"{k} => {v}" for k, v in d.items()]
    return result