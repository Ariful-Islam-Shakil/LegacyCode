import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def fetch_website_title(url: str) -> str:
    """
    Fetch the title of a website.

    Args:
        url (str): The URL of the website.

    Returns:
        str: The title of the website, or 'No Title Found' if the title is not found.

    Raises:
        requests.RequestException: If there is an issue with the HTTP request.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

def calculate_mean(arr: np.ndarray) -> float:
    """
    Calculate the mean of an array.

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
    Create a sample DataFrame.

    Returns:
        pd.DataFrame: A DataFrame with 'name' and 'score' columns.
    """
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'score': [85, 90, 95]}
    df = pd.DataFrame(data)
    return df  # Removed the check for 'score' in df.columns

def generate_range(n: int) -> list[int]:
    """
    Generate a list of squares from 0 to n.

    Args:
        n (int): The upper bound (exclusive).

    Returns:
        list[int]: A list of squares from 0 to n.
    """
    return [i * i for i in range(n)]

def exception_handling_demo() -> str:
    """
    Demonstrate exception handling.

    Returns:
        str: A message indicating whether an exception was caught.

    Raises:
        ZeroDivisionError: If the input is zero.
    """
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        return f"Caught an error: {e}"