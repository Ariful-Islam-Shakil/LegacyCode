# utils.py

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from io import StringIO

def fetch_website_title(url: str) -> str:
    """Get website title using requests + BeautifulSoup.

    Args:
        url (str): URL of the website.

    Returns:
        str: Website title or 'No Title Found' if not found.

    Raises:
        requests.RequestException: If there's an issue with the request.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

def calculate_mean(arr: np.ndarray) -> float:
    """Calculate mean using numpy.

    Args:
        arr (np.ndarray): Input array.

    Returns:
        float: Mean value of the array.
    """
    return np.mean(arr)

def create_dataframe() -> pd.DataFrame:
    """Create pandas DataFrame and check if 'score' column exists.

    Returns:
        pd.DataFrame: DataFrame with 'score' column or an empty DataFrame.
    """
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'score': [85, 90, 95]}
    df = pd.DataFrame(data)
    return df if 'score' in df.columns else pd.DataFrame()

def count_words(text: str) -> Counter:
    """Count word frequency using collections.Counter.

    Args:
        text (str): Input text.

    Returns:
        Counter: Word frequency Counter.
    """
    words = text.lower().split()
    return Counter(words)

def say_hello(name: str) -> str:
    """Greet someone using string formatting.

    Args:
        name (str): Name of the person.

    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}!"

def generate_range(n: int) -> list[int]:
    """Generate squares using a list comprehension.

    Args:
        n (int): Upper limit for the range.

    Returns:
        list[int]: List of squares.
    """
    return [i * i for i in range(n)]

def string_io_example() -> str:
    """StringIO example for string buffer.

    Returns:
        str: Content of the string buffer.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.12 with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration(d: dict[str, int]) -> list[str]:
    """Iterate dictionary with items().

    Args:
        d (dict[str, int]): Input dictionary.

    Returns:
        list[str]: List of key-value pairs.
    """
    return [f"{k} => {v}" for k, v in d.items()]

def exception_handling_demo() -> str:
    """Python 3 style exception handling.

    Returns:
        str: Result of the exception handling test.
    """
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        return f"Caught an error: {str(e)}"

# main.py

import utils

def main():
    print(utils.say_hello("Python 3.12 User"))

    title = utils.fetch_website_title("https://www.example.com")
    print(f"Website Title: {title}")

    mean_val = utils.calculate_mean([5, 15, 25])
    print(f"Mean Value: {mean_val}")

    df = utils.create_dataframe()
    print(f"DataFrame:\n{df}")

    # result = utils.plot_scores()
    # print(result)

    text = "Python is fun and Python is powerful"
    word_count = utils.count_words(text)
    print("Word Counts:")
    for word, count in word_count.items():  # Python 3 style dictionary iteration
        print(f"{word}: {count}")

    print(f"Generated Range Squares: {utils.generate_range(5)}")

    print(f"StringIO Buffer Output:\n{utils.string_io_example()}")

    print("Dictionary Iteration Output:")
    for line in utils.dictionary_iteration({'a': 1, 'b': 2}):
        print(line)

    print(f"Exception Handling Test: {utils.exception_handling_demo()}")

if __name__ == '__main__':
    main()