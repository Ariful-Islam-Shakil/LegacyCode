import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def fetch_website_title(url: str) -> str:
    """
    Fetch the title of a given website.

    Args:
        url (str): The URL of the website.

    Returns:
        str: The title of the website. If no title is found, returns 'No Title Found'.

    Raises:
        requests.RequestException: If the request to the website fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        raise
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

def calculate_mean(arr: np.ndarray) -> float:
    """
    Calculate the mean of a given array.

    Args:
        arr (np.ndarray): The input array.

    Returns:
        float: The mean of the array.

    Raises:
        TypeError: If the input is not a numpy array.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError("Input must be a numpy array")
    return np.mean(arr)

def create_dataframe() -> pd.DataFrame:
    """
    Create a sample dataframe.

    Returns:
        pd.DataFrame: A sample dataframe with 'name' and 'score' columns.
    """
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'score': [85, 90, 95]}
    return pd.DataFrame(data)

def generate_range(n: int) -> list[int]:
    """
    Generate a list of squares from 0 to n-1.

    Args:
        n (int): The upper bound (exclusive).

    Returns:
        list[int]: A list of squares from 0 to n-1.
    """
    return [i ** 2 for i in range(n)]

def exception_handling_demo() -> str:
    """
    Demonstrate exception handling.

    Returns:
        str: A message indicating whether an exception was caught.

    Raises:
        ZeroDivisionError: If division by zero occurs.
    """
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        return f"Caught an error: {str(e)}"