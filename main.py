from typing import Dict, List, Tuple
from dataclasses import dataclass
from io import StringIO
from urllib.parse import urlparse
from typing import Any
from collections import defaultdict
from math import prod
from typing import Generator

import pandas as pd
import numpy as np

@dataclass
class WebsiteTitle:
    """Class to hold the website title."""
    title: str

def say_hello(name: str) -> str:
    """Print a greeting message and return it.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"

def fetch_website_title(url: str) -> WebsiteTitle:
    """Fetch the title of a website.

    Args:
        url (str): The URL of the website.

    Returns:
        WebsiteTitle: A class containing the website title.

    Raises:
        ValueError: If the URL is invalid.
    """
    try:
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError("Invalid URL")
        # Simulate fetching the website title
        return WebsiteTitle(title="Example Website")
    except ValueError as e:
        raise e

def calculate_mean(numbers: List[float]) -> float:
    """Calculate the mean of a list of numbers.

    Args:
        numbers (List[float]): The list of numbers.

    Returns:
        float: The mean of the numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list is empty")
    return sum(numbers) / len(numbers)

def create_dataframe() -> pd.DataFrame:
    """Create a sample DataFrame.

    Returns:
        pd.DataFrame: A sample DataFrame.
    """
    data = {
        "Name": ["John", "Anna", "Peter"],
        "Age": [28, 24, 35]
    }
    return pd.DataFrame(data)

def count_words(text: str) -> Dict[str, int]:
    """Count the occurrences of each word in a given text.

    Args:
        text (str): The text to count words from.

    Returns:
        Dict[str, int]: A dictionary containing the word counts.
    """
    words = text.split()
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    return dict(word_count)

def generate_range(n: int) -> List[int]:
    """Generate a list of squares from 1 to n.

    Args:
        n (int): The upper limit.

    Returns:
        List[int]: A list of squares.
    """
    return [i ** 2 for i in range(1, n + 1)]

def string_io_example() -> str:
    """Demonstrate using StringIO.

    Returns:
        str: The output of the StringIO example.
    """
    buffer = StringIO()
    buffer.write("Hello, World!\n")
    buffer.write("This is a test.\n")
    buffer.seek(0)
    return buffer.read()

def dictionary_iteration() -> Generator[str, None, None]:
    """Demonstrate iterating over a dictionary.

    Yields:
        str: Each key-value pair in the dictionary.
    """
    data = {"a": 1, "b": 2, "c": 3}
    for key, value in data.items():
        yield f"{key}: {value}"

def exception_handling_demo() -> str:
    """Demonstrate exception handling.

    Returns:
        str: The result of the exception handling demo.
    """
    try:
        # Simulate an exception
        raise ValueError("Test exception")
    except ValueError as e:
        return str(e)

def main() -> None:
    """The main function."""
    print(say_hello("Python 3.12 User"))

    title = fetch_website_title("https://www.example.com")
    print(f"Website Title: {title.title}")

    mean_val = calculate_mean([5, 15, 25])
    print(f"Mean Value: {mean_val}")

    df = create_dataframe()
    print("DataFrame:\n", df)

    text = "Python is fun and Python is powerful"
    word_count = count_words(text)
    print("Word Counts:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    print("Generated Range Squares:", generate_range(5))

    print("StringIO Buffer Output:\n" + string_io_example())

    print("Dictionary Iteration Output:")
    for line in dictionary_iteration():
        print(line)

    print("Exception Handling Test:", exception_handling_demo())

if __name__ == '__main__':
    main()