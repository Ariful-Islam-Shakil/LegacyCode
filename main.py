from typing import Dict, List, Tuple
from dataclasses import dataclass
from io import StringIO
from urllib.parse import urlparse
from typing import Optional

import pandas as pd
from scipy import stats

class StringUtils:
    @staticmethod
    def say_hello(name: str) -> str:
        """
        Prints a greeting message.

        Args:
            name (str): The name of the person to greet.

        Returns:
            str: A greeting message.
        """
        return f"Hello, {name}!"

    @staticmethod
    def count_words(text: str) -> Dict[str, int]:
        """
        Counts the occurrences of each word in a given text.

        Args:
            text (str): The text to count words from.

        Returns:
            Dict[str, int]: A dictionary with words as keys and their counts as values.
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
            str: The contents of the StringIO buffer.
        """
        buffer = StringIO()
        buffer.write("Hello, World!\n")
        buffer.write("This is a test.\n")
        buffer.seek(0)
        return buffer.read()

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """
        Demonstrates dictionary iteration.

        Returns:
            List[str]: A list of dictionary keys.
        """
        data = {"key1": "value1", "key2": "value2"}
        return list(data.keys())

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
            # Simulate a web request
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
        return stats.tmean(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """
        Creates a sample DataFrame.

        Returns:
            pd.DataFrame: The sample DataFrame.
        """
        data = {"A": [1, 2, 3], "B": [4, 5, 6]}
        return pd.DataFrame(data)

    @staticmethod
    def generate_range(n: int) -> List[Tuple[int, int]]:
        """
        Generates a range of numbers and squares them.

        Args:
            n (int): The number of elements in the range.

        Returns:
            List[Tuple[int, int]]: A list of tuples, where each tuple contains a number and its square.
        """
        return [(i, i**2) for i in range(n)]

    @staticmethod
    def exception_handling_demo() -> str:
        """
        Demonstrates exception handling.

        Returns:
            str: A message indicating whether the exception was handled.
        """
        try:
            # Simulate an exception
            raise ValueError("Test exception")
        except ValueError:
            return "Exception handled"
        else:
            return "No exception occurred"

def main():
    print(StringUtils.say_hello("Python 3.12 User"))

    title = MathUtils.fetch_website_title("https://www.example.com")
    print("Website Title:", title)

    mean_val = MathUtils.calculate_mean([5, 15, 25])
    print("Mean Value:", mean_val)

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