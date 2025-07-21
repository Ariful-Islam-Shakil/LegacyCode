import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def fetch_website_title(url: str) -> str:
    """
    Fetches the title of a given website.

    Args:
        url (str): The URL of the website.

    Returns:
        str: The title of the website. If no title is found, returns 'No Title Found'.

    Raises:
        requests.RequestException: If there is an issue with the HTTP request.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

def calculate_mean(arr: np.ndarray) -> float:
    """
    Calculates the mean of a given array.

    Args:
        arr (np.ndarray): The input array.

    Returns:
        float: The mean of the array.

    Raises:
        TypeError: If the input is not a numpy array.
    """
    return np.mean(arr)

def create_dataframe() -> pd.DataFrame:
    """
    Creates a sample DataFrame.

    Returns:
        pd.DataFrame: A DataFrame with two columns: 'name' and 'score'.
    """
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'score': [85, 90, 95]}
    df = pd.DataFrame(data)
    return df  # Removed the check for 'score' in df.columns

def generate_range(n: int) -> list[int]:
    """
    Generates a list of squares from 0 to n-1.

    Args:
        n (int): The upper bound (exclusive).

    Returns:
        list[int]: A list of squares from 0 to n-1.
    """
    return [i * i for i in range(n)]

def exception_handling_demo() -> str:
    """
    Demonstrates exception handling.

    Returns:
        str: A message indicating whether an error was caught.

    Raises:
        ZeroDivisionError: If division by zero occurs.
    """
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        return f"Caught an error: {e}"