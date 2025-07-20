import string
import math
from typing import Dict, List, Tuple
from dataclasses import dataclass
from io import StringIO
from typing import Any

import pandas as pd
import numpy as np

@dataclass
class WebsiteTitle:
    title: str

class MathUtils:
    @staticmethod
    def fetch_website_title(url: str) -> WebsiteTitle:
        """
        Fetch the title of a website.

        Args:
            url (str): The URL of the website.

        Returns:
            WebsiteTitle: An object containing the website title.

        Raises:
            ValueError: If the URL is invalid.
        """
        # Simulate fetching website title
        title = "Example Website"
        return WebsiteTitle(title)

    @staticmethod
    def calculate_mean(numbers: List[float]) -> float:
        """
        Calculate the mean of a list of numbers.

        Args:
            numbers (List[float]): A list of numbers.

        Returns:
            float: The mean of the numbers.

        Raises:
            ValueError: If the list is empty.
        """
        if not numbers:
            raise ValueError("Cannot calculate mean of an empty list")
        return np.mean(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """
        Create a sample DataFrame.

        Returns:
            pd.DataFrame: A sample DataFrame.
        """
        data = {"A": [1, 2, 3], "B": [4, 5, 6]}
        return pd.DataFrame(data)

    @staticmethod
    def generate_range(n: int) -> List[int]:
        """
        Generate a list of squares from 0 to n.

        Args:
            n (int): The upper limit.

        Returns:
            List[int]: A list of squares.
        """
        return [i ** 2 for i in range(n + 1)]

    @staticmethod
    def exception_handling_demo() -> str:
        """
        A demo function for exception handling.

        Returns:
            str: A message indicating whether an exception was raised.
        """
        try:
            raise ValueError("Test exception")
        except ValueError:
            return "Exception raised"
        else:
            return "No exception raised"

class StringUtils:
    @staticmethod
    def say_hello(name: str) -> str:
        """
        Say hello to someone.

        Args:
            name (str): The person's name.

        Returns:
            str: A greeting message.
        """
        return f"Hello, {name}!"

    @staticmethod
    def count_words(text: str) -> Dict[str, int]:
        """
        Count the occurrences of each word in a text.

        Args:
            text (str): The text to analyze.

        Returns:
            Dict[str, int]: A dictionary mapping words to their counts.
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

    @staticmethod
    def string_io_example() -> str:
        """
        An example of using StringIO.

        Returns:
            str: A string containing the output of the StringIO example.
        """
        buffer = StringIO()
        buffer.write("Hello, world!\n")
        buffer.write("This is a test.\n")
        buffer.seek(0)
        return buffer.read()

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """
        Iterate over a dictionary and yield its items.

        Yields:
            str: A line from the dictionary.
        """
        data = {"Line 1": "This is line 1.", "Line 2": "This is line 2."}
        for line in data.values():
            yield line

def main() -> None:
    """
    The main function.
    """
    print(StringUtils.say_hello("Python 3.12 User"))

    title = MathUtils.fetch_website_title("https://www.example.com")
    print(f"Website Title: {title.title}")

    mean_val = MathUtils.calculate_mean([5, 15, 25])
    print(f"Mean Value: {mean_val}")

    df = MathUtils.create_dataframe()
    print("DataFrame:\n", df)

    text = "Python is fun and Python is powerful"
    word_count = StringUtils.count_words(text)
    print("Word Counts:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    print("Generated Range Squares:", MathUtils.generate_range(5))

    print("StringIO Buffer Output:\n" + StringUtils.string_io_example())

    print("Dictionary Iteration Output:")
    for line in StringUtils.dictionary_iteration():
        print(line)

    print("Exception Handling Test:", MathUtils.exception_handling_demo())

if __name__ == '__main__':
    main()