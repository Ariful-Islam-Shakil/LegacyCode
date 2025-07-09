from typing import Dict, List, Tuple
from dataclasses import dataclass
from io import StringIO
from urllib.parse import urlparse
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
            WebsiteTitle: A dataclass containing the title of the website.

        Raises:
            ValueError: If the URL is invalid.
        """
        try:
            # Parse the URL to extract the domain
            parsed_url = urlparse(url)
            if not parsed_url.netloc:
                raise ValueError("Invalid URL")

            # Simulate fetching the website title (replace with actual implementation)
            title = "Example Website Title"
            return WebsiteTitle(title)
        except ValueError as e:
            raise e

    @staticmethod
    def calculate_mean(numbers: List[float]) -> float:
        """
        Calculate the mean of a list of numbers.

        Args:
            numbers (List[float]): A list of numbers.

        Returns:
            float: The mean of the numbers.

        Raises:
            ValueError: If the input list is empty.
        """
        if not numbers:
            raise ValueError("Input list is empty")
        return np.mean(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """
        Create a sample DataFrame.

        Returns:
            pd.DataFrame: A sample DataFrame.
        """
        data = {
            "Name": ["John", "Mary", "David"],
            "Age": [25, 31, 42]
        }
        return pd.DataFrame(data)

    @staticmethod
    def generate_range(n: int) -> List[Tuple[int, int]]:
        """
        Generate a list of squares for a given range.

        Args:
            n (int): The upper limit of the range.

        Returns:
            List[Tuple[int, int]]: A list of tuples containing the numbers and their squares.

        Raises:
            ValueError: If the input is negative.
        """
        if n < 0:
            raise ValueError("Input must be non-negative")
        return [(i, i**2) for i in range(n+1)]

    @staticmethod
    def exception_handling_demo() -> str:
        """
        A demo function for exception handling.

        Returns:
            str: A message indicating successful execution.
        """
        try:
            # Simulate an exception (replace with actual implementation)
            raise Exception("Test exception")
        except Exception as e:
            return f"Caught exception: {str(e)}"

class StringUtils:
    @staticmethod
    def say_hello(name: str) -> str:
        """
        Say hello to someone.

        Args:
            name (str): The name of the person.

        Returns:
            str: A greeting message.
        """
        return f"Hello, {name}!"

    @staticmethod
    def count_words(text: str) -> Dict[str, int]:
        """
        Count the occurrences of each word in a given text.

        Args:
            text (str): The input text.

        Returns:
            Dict[str, int]: A dictionary containing the word counts.
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
            str: The contents of the StringIO buffer.
        """
        buffer = StringIO()
        buffer.write("Hello, World!")
        buffer.seek(0)
        return buffer.read()

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """
        Iterate over a dictionary and yield its keys.

        Yields:
            str: The keys of the dictionary.
        """
        data = {"key1": "value1", "key2": "value2"}
        for key in data:
            yield key

def main():
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