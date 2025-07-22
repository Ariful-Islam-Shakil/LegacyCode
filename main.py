import string
import math
from typing import Dict, List, Tuple
from dataclasses import dataclass
from io import StringIO
from typing import Generator

import pandas as pd

@dataclass
class WebsiteTitle:
    title: str

def say_hello(name: str) -> str:
    """
    Prints a personalized greeting message.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

def fetch_website_title(url: str) -> WebsiteTitle:
    """
    Fetches the title of a website.

    Args:
        url (str): The URL of the website.

    Returns:
        WebsiteTitle: The title of the website.
    """
    # Simulate fetching the website title
    return WebsiteTitle("Example Website Title")

def calculate_mean(numbers: List[float]) -> float:
    """
    Calculates the mean of a list of numbers.

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: The mean of the numbers.
    """
    return sum(numbers) / len(numbers)

def create_dataframe() -> pd.DataFrame:
    """
    Creates a sample DataFrame.

    Returns:
        pd.DataFrame: A sample DataFrame.
    """
    data = {
        "Name": ["John", "Anna", "Peter"],
        "Age": [28, 24, 35]
    }
    return pd.DataFrame(data)

def count_words(text: str) -> Dict[str, int]:
    """
    Counts the occurrences of each word in a given text.

    Args:
        text (str): The text to count words from.

    Returns:
        Dict[str, int]: A dictionary with words as keys and their counts as values.
    """
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def generate_range(n: int) -> Generator[int, None, None]:
    """
    Generates a range of numbers and squares them.

    Args:
        n (int): The number of elements in the range.

    Yields:
        int: The square of each number in the range.
    """
    for i in range(n):
        yield i ** 2

def string_io_example() -> str:
    """
    Demonstrates using StringIO.

    Returns:
        str: A string generated from the StringIO buffer.
    """
    buffer = StringIO()
    buffer.write("Hello, World!")
    buffer.seek(0)
    return buffer.read()

def dictionary_iteration() -> Generator[str, None, None]:
    """
    Iterates over a dictionary and yields each key-value pair.

    Yields:
        str: Each key-value pair in the dictionary.
    """
    dictionary = {"key1": "value1", "key2": "value2"}
    for key, value in dictionary.items():
        yield f"{key}: {value}"

def exception_handling_demo() -> str:
    """
    Demonstrates exception handling.

    Returns:
        str: A message indicating whether the exception was handled.
    """
    try:
        # Simulate an exception
        raise Exception("Test exception")
    except Exception as e:
        return f"Exception handled: {str(e)}"
    else:
        return "No exception occurred"

def main() -> None:
    """
    The main entry point of the program.
    """
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

    print("Generated Range Squares:", list(generate_range(5)))

    print("StringIO Buffer Output:\n" + string_io_example())

    print("Dictionary Iteration Output:")
    for line in dictionary_iteration():
        print(line)

    print("Exception Handling Test:", exception_handling_demo())

if __name__ == '__main__':
    main()