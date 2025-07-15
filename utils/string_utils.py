from io import StringIO
from collections import Counter

def say_hello(name: str) -> str:
    """Returns a greeting message with the given name.

    Args:
        name (str): The name to be used in the greeting.

    Returns:
        str: A greeting message with the given name.

    Raises:
        TypeError: If the name is not a string.
    """
    return f"Hello, {name}!"

def count_words(text: str) -> Counter:
    """Counts the occurrences of each word in the given text.

    Args:
        text (str): The text to be analyzed.

    Returns:
        Counter: A dictionary-like object containing the word counts.

    Raises:
        TypeError: If the text is not a string.
    """
    return Counter(text.lower().split())

def string_io_example() -> str:
    """Demonstrates the usage of StringIO for creating a string buffer.

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
    """Iterates over a dictionary and returns a list of key-value pairs.

    Args:
        d (dict[str, int]): The dictionary to be iterated.

    Returns:
        list[str]: A list of key-value pairs as strings.

    Raises:
        TypeError: If the input is not a dictionary.
    """
    return [f"{k} => {v}" for k, v in d.items()]