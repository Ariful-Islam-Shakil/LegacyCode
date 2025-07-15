from io import StringIO
from collections import Counter

def say_hello(name: str) -> str:
    """
    Returns a greeting message with the given name.

    Args:
        name (str): The person's name.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

def count_words(text: str) -> Counter:
    """
    Counts the occurrences of each word in the given text.

    Args:
        text (str): The text to count words from.

    Returns:
        Counter: A dictionary-like object containing word counts.
    """
    words = text.lower().split()
    return Counter(words)

def string_io_example() -> str:
    """
    Demonstrates the use of StringIO for string buffering.

    Returns:
        str: The content of the string buffer.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.12 with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration(dictionary: dict[str, int]) -> list[str]:
    """
    Iterates over a dictionary and returns a list of key-value pairs.

    Args:
        dictionary (dict[str, int]): The dictionary to iterate over.

    Returns:
        list[str]: A list of key-value pairs as strings.
    """
    result = []
    for k, v in dictionary.items():
        result.append(f"{k} => {v}")
    return result