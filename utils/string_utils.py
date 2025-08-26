from collections import Counter
from io import StringIO

def say_hello(name: str) -> str:
    """
    Returns a personalized greeting message.

    Args:
        name (str): The name to be used in the greeting.

    Returns:
        str: A greeting message with the provided name.
    """
    return f"Hello, {name}!"

def count_words(text: str) -> Counter:
    """
    Counts the occurrences of each word in a given text.

    Args:
        text (str): The text to be analyzed.

    Returns:
        Counter: A counter object with words as keys and their counts as values.
    """
    words = text.lower().split()
    return Counter(words)

def string_io_example() -> str:
    """
    Demonstrates the use of StringIO to create a string buffer.

    Returns:
        str: The content of the string buffer.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.x with io module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration() -> list:
    """
    Iterates over a dictionary and returns a list of key-value pairs as strings.

    Returns:
        list: A list of strings representing key-value pairs.
    """
    d = {'a': 1, 'b': 2}
    result = []
    for k, v in d.items():
        result.append(f"{k} => {v}")
    return result