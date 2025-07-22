from io import StringIO
from collections import Counter

def say_hello(name: str) -> str:
    """Return a greeting message with the given name.

    Args:
        name (str): The name to include in the greeting.

    Returns:
        str: A greeting message with the given name.

    Raises:
        TypeError: If the name is not a string.
    """
    return f"Hello, {name}!"

def count_words(text: str) -> Counter:
    """Count the occurrences of each word in the given text.

    Args:
        text (str): The text to count words from.

    Returns:
        Counter: A dictionary-like object with word counts.

    Raises:
        TypeError: If the text is not a string.
    """
    words = text.lower().split()
    return Counter(words)

def string_io_example() -> str:
    """Demonstrate using a StringIO object to write and read a string.

    Returns:
        str: The content written to the StringIO object.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.12 with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration(dictionary: dict[str, int]) -> list[str]:
    """Iterate over a dictionary and return a list of key-value pairs.

    Args:
        dictionary (dict[str, int]): The dictionary to iterate over.

    Returns:
        list[str]: A list of key-value pairs as strings.

    Raises:
        TypeError: If the dictionary is not a mapping.
    """
    result = []
    for k, v in dictionary.items():
        result.append(f"{k} => {v}")
    return result