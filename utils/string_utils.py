from io import StringIO
from collections import Counter

def say_hello(name: str) -> str:
    """Return a personalized greeting.

    Args:
        name (str): The name to include in the greeting.

    Returns:
        str: A greeting message with the provided name.
    """
    return f"Hello, {name}!"

def count_words(text: str) -> Counter:
    """Count the occurrences of each word in the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        Counter: A dictionary-like object with word counts.
    """
    words = text.lower().split()
    return Counter(words)

def string_io_example() -> str:
    """Demonstrate using StringIO for string buffering.

    Returns:
        str: The contents of the string buffer.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.x with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration() -> list[str]:
    """Iterate over a dictionary and return key-value pairs as strings.

    Returns:
        list[str]: A list of key-value pair strings.
    """
    d = {'a': 1, 'b': 2}
    result = [f"{k} => {v}" for k, v in d.items()]
    return result