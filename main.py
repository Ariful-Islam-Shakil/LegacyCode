import string
import math
from typing import Dict, List, Tuple
from dataclasses import dataclass
from io import StringIO
from urllib.parse import urlparse
from typing import Optional

import pandas as pd
import numpy as np

@dataclass
class WebsiteTitle:
    title: str

class StringUtils:
    @staticmethod
    def say_hello(name: str) -> str:
        """
        Prints a greeting message.

        Args:
            name (str): The name to be used in the greeting.

        Returns:
            str: The greeting message.
        """
        return f"Hello, {name}!"

    @staticmethod
    def count_words(text: str) -> Dict[str, int]:
        """
        Counts the occurrences of each word in the given text.

        Args:
            text (str): The text to be analyzed.

        Returns:
            Dict[str, int]: A dictionary where the keys are the words and the values are their respective counts.
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
        Demonstrates the usage of StringIO.

        Returns:
            str: The output of the StringIO buffer.
        """
        buffer = StringIO()
        buffer.write("Hello, World!")
        buffer.seek(0)
        return buffer.read()

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """
        Demonstrates dictionary iteration.

        Returns:
            List[str]: A list of lines from the dictionary.
        """
        dictionary = {"key1": "value1", "key2": "value2"}
        lines = []
        for key, value in dictionary.items():
            lines.append(f"{key}: {value}")
        return lines

class MathUtils:
    @staticmethod
    def fetch_website_title(url: str) -> Optional[str]:
        """
        Fetches the title of a website.

        Args:
            url (str): The URL of the website.

        Returns:
            Optional[str]: The title of the website, or None if it cannot be fetched.
        """
        try:
            # Simulate a website title fetch
            parsed_url = urlparse(url)
            return f"Title of {parsed_url.netloc}"
        except Exception as e:
            return None

    @staticmethod
    def calculate_mean(numbers: List[float]) -> float:
        """
        Calculates the mean of a list of numbers.

        Args:
            numbers (List[float]): The list of numbers.

        Returns:
            float: The mean of the numbers.
        """
        return np.mean(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """
        Creates a sample DataFrame.

        Returns:
            pd.DataFrame: The sample DataFrame.
        """
        data = {
            "Name": ["John", "Anna", "Peter"],
            "Age": [28, 24, 35]
        }
        return pd.DataFrame(data)

    @staticmethod
    def generate_range(n: int) -> List[int]:
        """
        Generates a range of numbers.

        Args:
            n (int): The number of elements in the range.

        Returns:
            List[int]: The generated range.
        """
        return list(range(n))

    @staticmethod
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

def main():
    print(StringUtils.say_hello("Python 3.12 User"))

    title = MathUtils.fetch_website_title("https://www.example.com")
    print(f"Website Title: {title}")

    mean_val = MathUtils.calculate_mean([5, 15, 25])
    print(f"Mean Value: {mean_val}")

    df = MathUtils.create_dataframe()
    print("DataFrame:\n", df)

    text = "Python is fun and Python is powerful"
    word_count = StringUtils.count_words(text)
    print("Word Counts:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    print("Generated Range Squares:", [i**2 for i in MathUtils.generate_range(5)])

    print("StringIO Buffer Output:\n" + StringUtils.string_io_example())

    print("Dictionary Iteration Output:")
    for line in StringUtils.dictionary_iteration():
        print(line)

    print("Exception Handling Test:", MathUtils.exception_handling_demo())

if __name__ == '__main__':
    main()