from io import StringIO
from collections import Counter

def say_hello(name: str) -> str:
    """Returns a greeting message with the provided name.

    Args:
        name (str): The name to be used in the greeting.

    Returns:
        str: A greeting message.
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
    """Demonstrates the usage of StringIO for string buffering.

    Returns:
        str: The content of the string buffer.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.12 with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration(d: dict[str, int]) -> list[str]:
    """Iterates over a dictionary and returns a list of key-value pairs.

    Args:
        d (dict[str, int]): The dictionary to be iterated.

    Returns:
        list[str]: A list of key-value pairs as strings.
    """
    result = []
    for k, v in d.items():
        result.append(f"{k} => {v}")
    return result