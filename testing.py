import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from io import StringIO

def fetch_website_title(url: str) -> str:
    """
    Get website title using requests + BeautifulSoup.

    Args:
        url (str): Website URL.

    Returns:
        str: Website title.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

def calculate_mean(arr: list[float]) -> float:
    """
    Calculate mean using numpy.

    Args:
        arr (list[float]): List of numbers.

    Returns:
        float: Mean value.
    """
    return np.mean(arr)

def create_dataframe() -> pd.DataFrame:
    """
    Create pandas DataFrame and check if 'score' column exists.

    Returns:
        pd.DataFrame: DataFrame with 'name' and 'score' columns.
    """
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'score': [85, 90, 95]}
    df = pd.DataFrame(data)
    if 'score' in df.columns:
        return df
    return pd.DataFrame()

def count_words(text: str) -> Counter:
    """
    Count word frequency using collections.Counter.

    Args:
        text (str): Input text.

    Returns:
        Counter: Word frequency counter.
    """
    words = text.lower().split()
    return Counter(words)

def say_hello(name: str) -> str:
    """
    Greeting using f-string.

    Args:
        name (str): Name.

    Returns:
        str: Greeting message.
    """
    return f"Hello, {name}!"

def generate_range(n: int) -> list[int]:
    """
    Generate squares.

    Args:
        n (int): Number of squares.

    Returns:
        list[int]: List of squares.
    """
    return [i * i for i in range(n)]

def string_io_example() -> str:
    """
    StringIO example for string buffer.

    Returns:
        str: String buffer content.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration() -> list[str]:
    """
    Iterate dictionary.

    Returns:
        list[str]: Dictionary iteration output.
    """
    d = {'a': 1, 'b': 2}
    return [f"{k} => {v}" for k, v in d.items()]

def exception_handling_demo() -> str:
    """
    Python 3 style exception handling.

    Returns:
        str: Exception handling result.
    """
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        return f"Caught an error: {str(e)}"

def main() -> None:
    print(say_hello("Python 3 User"))

    title = fetch_website_title("https://www.example.com")
    print(f"Website Title: {title}")

    mean_val = calculate_mean([5, 15, 25])
    print(f"Mean Value: {mean_val}")

    df = create_dataframe()
    print(f"DataFrame:\n{df}")

    text = "Python is fun and Python is powerful"
    word_count = count_words(text)
    print("Word Counts:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    print(f"Generated Range Squares: {generate_range(5)}")

    print(f"StringIO Buffer Output:\n{string_io_example()}")

    print("Dictionary Iteration Output:")
    for line in dictionary_iteration():
        print(line)

    print(f"Exception Handling Test: {exception_handling_demo()}")

if __name__ == '__main__':
    main()