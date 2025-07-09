import string
import math
import pandas as pd
from typing import Dict, List, Tuple, Any

class MathUtils:
    """Provides utility functions for mathematical operations."""

    @staticmethod
    def fetch_website_title(url: str) -> str:
        """Fetches the title of a website given its URL.

        Args:
            url (str): The URL of the website.

        Returns:
            str: The title of the website.

        Raises:
            ValueError: If the URL is invalid.
        """
        # Replace this with a real implementation to fetch website title
        return "Example Website Title"

    @staticmethod
    def calculate_mean(numbers: List[float]) -> float:
        """Calculates the mean of a list of numbers.

        Args:
            numbers (List[float]): A list of numbers.

        Returns:
            float: The mean of the numbers.

        Raises:
            ValueError: If the input list is empty.
        """
        if not numbers:
            raise ValueError("Input list is empty")
        return sum(numbers) / len(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """Creates an empty pandas DataFrame.

        Returns:
            pd.DataFrame: An empty DataFrame.
        """
        return pd.DataFrame()

    @staticmethod
    def generate_range(n: int) -> List[int]:
        """Generates a list of squares of numbers from 0 to n.

        Args:
            n (int): The upper limit.

        Returns:
            List[int]: A list of squares.
        """
        return [i ** 2 for i in range(n + 1)]

    @staticmethod
    def exception_handling_demo() -> str:
        """Demonstrates exception handling.

        Returns:
            str: A message indicating successful exception handling.
        """
        try:
            # Simulate an exception
            raise ValueError("Test exception")
        except ValueError as e:
            return f"Caught exception: {e}"
        return "No exception caught"


class StringUtils:
    """Provides utility functions for string operations."""

    @staticmethod
    def say_hello(name: str) -> str:
        """Prints a greeting message.

        Args:
            name (str): The name of the person.

        Returns:
            str: A greeting message.
        """
        return f"Hello, {name}!"

    @staticmethod
    def count_words(text: str) -> Dict[str, int]:
        """Counts the occurrences of each word in a given text.

        Args:
            text (str): The input text.

        Returns:
            Dict[str, int]: A dictionary with word counts.
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
        """Demonstrates using StringIO.

        Returns:
            str: A message indicating successful StringIO usage.
        """
        # Replace this with a real implementation using StringIO
        return "StringIO example"

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """Demonstrates dictionary iteration.

        Returns:
            List[str]: A list of lines from a dictionary.
        """
        # Replace this with a real implementation using dictionary iteration
        return ["Line 1", "Line 2", "Line 3"]


def main() -> None:
    """The main function."""
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

    print("Generated Range Squares:", MathUtils.generate_range(5))

    print("StringIO Buffer Output:\n" + StringUtils.string_io_example())

    print("Dictionary Iteration Output:")
    for line in StringUtils.dictionary_iteration():
        print(line)

    print("Exception Handling Test:", MathUtils.exception_handling_demo())


if __name__ == '__main__':
    main()