from io import StringIO
from collections import Counter

def say_hello(name: str) -> str:
    """
    Returns a personalized greeting message.

    Args:
        name (str): The name to include in the greeting.

    Returns:
        str: A greeting message with the provided name.
    """
    return f"Hello, {name}!"

def count_words(text: str) -> Counter:
    """
    Counts the occurrences of each word in the provided text.

    Args:
        text (str): The text to count words from.

    Returns:
        Counter: A dictionary-like object with word frequencies.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input text must be a string")
    words = text.lower().split()
    return Counter(words)

def string_io_example() -> str:
    """
    Demonstrates the use of StringIO for string buffering.

    Returns:
        str: The contents of the string buffer.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.x with io module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration(d: dict[str, int]) -> list[str]:
    """
    Iterates over a dictionary and returns a list of key-value pairs.

    Args:
        d (dict[str, int]): The dictionary to iterate over.

    Returns:
        list[str]: A list of key-value pairs as strings.

    Raises:
        TypeError: If the input dictionary is not a mapping.
    """
    if not isinstance(d, dict):
        raise TypeError("Input must be a mapping")
    result = []
    for k, v in d.items():
        result.append(f"{k} => {v}")
    return result