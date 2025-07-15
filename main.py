import string
import math
import pandas as pd
from typing import Dict, List, Tuple

class StringUtils:
    """Provides utility methods for string operations."""

    @staticmethod
    def say_hello(name: str) -> str:
        """Prints a greeting message with the given name.

        Args:
            name: The name to include in the greeting.

        Returns:
            The greeting message.
        """
        return f"Hello, {name}!"

    @staticmethod
    def count_words(text: str) -> Dict[str, int]:
        """Counts the occurrences of each word in the given text.

        Args:
            text: The text to analyze.

        Returns:
            A dictionary with word counts.
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
        """Demonstrates using StringIO for string output.

        Returns:
            A string generated using StringIO.
        """
        from io import StringIO
        buffer = StringIO()
        buffer.write("Hello, world!")
        buffer.seek(0)
        return buffer.read()

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """Iterates over a dictionary and prints its keys and values.

        Returns:
            A list of lines generated from the dictionary iteration.
        """
        dictionary = {"key1": "value1", "key2": "value2"}
        lines = []
        for key, value in dictionary.items():
            lines.append(f"{key}: {value}")
        return lines


class MathUtils:
    """Provides utility methods for mathematical operations."""

    @staticmethod
    def fetch_website_title(url: str) -> str:
        """Fetches the title of the given website.

        Args:
            url: The URL of the website.

        Returns:
            The title of the website.
        """
        # Simulate fetching the website title
        return "Example Website Title"

    @staticmethod
    def calculate_mean(numbers: List[float]) -> float:
        """Calculates the mean of the given numbers.

        Args:
            numbers: The numbers to calculate the mean from.

        Returns:
            The mean of the numbers.
        """
        return sum(numbers) / len(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """Creates a sample DataFrame.

        Returns:
            A sample DataFrame.
        """
        data = {"Name": ["John", "Mary", "David"], "Age": [25, 31, 42]}
        return pd.DataFrame(data)

    @staticmethod
    def generate_range(n: int) -> List[int]:
        """Generates a range of numbers and squares them.

        Args:
            n: The number of elements in the range.

        Returns:
            A list of squared numbers.
        """
        return [i ** 2 for i in range(n)]

    @staticmethod
    def exception_handling_demo() -> str:
        """Demonstrates exception handling.

        Returns:
            A message indicating successful exception handling.
        """
        try:
            # Simulate an exception
            raise ValueError("Test exception")
        except ValueError as e:
            return f"Caught exception: {e}"
        else:
            return "No exception occurred"


def main():
    """The main entry point of the program."""
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