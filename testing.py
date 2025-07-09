# utils.py

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from io import StringIO
from typing import Dict, List, Tuple

def fetch_website_title(url: str) -> str:
    """
    Get website title using requests + BeautifulSoup.

    Args:
        url (str): The URL of the website.

    Returns:
        str: The title of the website. If no title is found, returns 'No Title Found'.

    Raises:
        requests.RequestException: If there is an issue with the request.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

def calculate_mean(arr: List[float]) -> float:
    """
    Calculate mean using numpy.

    Args:
        arr (List[float]): The list of numbers.

    Returns:
        float: The mean of the numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    return np.mean(arr)

def create_dataframe() -> pd.DataFrame:
    """
    Create pandas DataFrame and check if 'score' column exists.

    Returns:
        pd.DataFrame: The DataFrame.
    """
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'score': [85, 90, 95]}
    df = pd.DataFrame(data)
    if 'score' in df.columns:
        return df
    return pd.DataFrame()

def count_words(text: str) -> Dict[str, int]:
    """
    Count word frequency using collections.Counter.

    Args:
        text (str): The text to count words from.

    Returns:
        Dict[str, int]: A dictionary with word frequencies.
    """
    words = text.lower().split()
    return Counter(words)

def say_hello(name: str) -> str:
    """
    Greet someone.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

def generate_range(n: int) -> List[int]:
    """
    Generate squares using a list comprehension.

    Args:
        n (int): The number of squares to generate.

    Returns:
        List[int]: A list of squares.
    """
    return [i * i for i in range(n)]

def string_io_example() -> str:
    """
    StringIO example for string buffer.

    Returns:
        str: The content of the string buffer.
    """
    buffer = StringIO()
    buffer.write("This is a string buffer.\n")
    buffer.write("Works in Python 3.12 with StringIO module.\n")
    content = buffer.getvalue()
    buffer.close()
    return content

def dictionary_iteration(d: Dict[str, int]) -> List[str]:
    """
    Iterate dictionary with items().

    Args:
        d (Dict[str, int]): The dictionary to iterate.

    Returns:
        List[str]: A list of key-value pairs as strings.
    """
    return [f"{k} => {v}" for k, v in d.items()]

def exception_handling_demo() -> str:
    """
    Exception handling demo.

    Returns:
        str: A message indicating whether an exception was caught.
    """
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        return f"Caught an error: {str(e)}"

# main.py

def main() -> None:
    """
    The main function.
    """
    print(say_hello("Python 3.12 User"))

    title = fetch_website_title("https://www.example.com")
    print("Website Title:", title)

    mean_val = calculate_mean([5, 15, 25])
    print("Mean Value:", mean_val)

    df = create_dataframe()
    print("DataFrame:\n", df)

    # result = utils.plot_scores()
    # print(result)

    text = "Python is fun and Python is powerful"
    word_count = count_words(text)
    print("Word Counts:")
    for word, count in word_count.items():  # Python 3 style dictionary iteration
        print(f"{word}: {count}")

    print("Generated Range Squares:", generate_range(5))

    print("StringIO Buffer Output:\n" + string_io_example())

    print("Dictionary Iteration Output:")
    for line in dictionary_iteration({'a': 1, 'b': 2}):
        print(line)

    print("Exception Handling Test:", exception_handling_demo())

if __name__ == '__main__':
    main()