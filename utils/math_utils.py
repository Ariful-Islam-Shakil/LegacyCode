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
        str: The title of the website if found, otherwise 'No Title Found'.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string if soup.title else 'No Title Found'

def calculate_mean(arr: np.ndarray) -> float:
    """
    Calculates the mean of a given numpy array.

    Args:
        arr (np.ndarray): The input array.

    Returns:
        float: The mean of the array.
    """
    return np.mean(arr)

def create_dataframe() -> pd.DataFrame:
    """
    Creates a sample pandas DataFrame.

    Returns:
        pd.DataFrame: A DataFrame with 'name' and 'score' columns.
    """
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'score': [85, 90, 95]}
    df = pd.DataFrame(data)
    if 'score' in df.columns:
        return df
    return pd.DataFrame()

def generate_range(n: int) -> list[int]:
    """
    Generates a list of squares of numbers from 0 to n-1.

    Args:
        n (int): The number of elements in the list.

    Returns:
        list[int]: A list of squares of numbers from 0 to n-1.
    """
    result = []
    for i in range(n):
        result.append(i * i)
    return result

def exception_handling_demo() -> str:
    """
    Demonstrates exception handling for ZeroDivisionError.

    Returns:
        str: An error message if an exception occurs.
    """
    try:
        return 10 / 0
    except ZeroDivisionError as e:
        return f"Caught an error: {str(e)}"