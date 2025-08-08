from collections import Counter
from io import StringIO

def say_hello(name: str) -> str:
    """
    Returns a personalized greeting message.

    Args:
        name (str): The name to be used in the greeting.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

def count_words(text: str) -> Counter:
    """
    Counts the occurrences of each word in a given text.

    Args:
        text (str): The text to be analyzed.

    Returns:
        Counter: A counter of word occurrences.
    """
    words = text.lower().split()
    return Counter(words)

def string_io_example() -> str:
    """
    Demonstrates the use of StringIO to create a string buffer.

    Returns:
        str: The contents of the string buffer.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.x with io module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration() -> list[str]:
    """
    Iterates over a dictionary and returns a list of key-value pairs.

    Returns:
        list[str]: A list of key-value pairs as strings.
    """
    d = {'a': 1, 'b': 2}
    result = []
    for k, v in d.items():
        result.append(f"{k} => {v}")
    return result