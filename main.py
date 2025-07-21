import string
import math
import pandas as pd
from typing import Dict, List, Tuple

class StringUtils:
    """String utility class."""
    
    @staticmethod
    def say_hello(name: str) -> str:
        """Prints a greeting message.

        Args:
            name (str): The name to be used in the greeting.

        Returns:
            str: The greeting message.
        """
        return f"Hello, {name}!"

    @staticmethod
    def count_words(text: str) -> Dict[str, int]:
        """Counts the occurrences of each word in a given text.

        Args:
            text (str): The text to be analyzed.

        Returns:
            Dict[str, int]: A dictionary where keys are words and values are their counts.
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
        """Demonstrates the usage of StringIO.

        Returns:
            str: A string containing the output of the StringIO example.
        """
        from io import StringIO
        buffer = StringIO()
        buffer.write("Hello, World!\n")
        buffer.write("This is a test.\n")
        buffer.seek(0)
        return buffer.read()

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """Iterates over a dictionary and prints its items.

        Returns:
            List[str]: A list of strings representing the dictionary items.
        """
        my_dict = {"key1": "value1", "key2": "value2"}
        result = []
        for key, value in my_dict.items():
            result.append(f"{key}: {value}")
        return result


class MathUtils:
    """Math utility class."""
    
    @staticmethod
    def fetch_website_title(url: str) -> str:
        """Fetches the title of a website.

        Args:
            url (str): The URL of the website.

        Returns:
            str: The title of the website.

        Raises:
            ValueError: If the URL is invalid.
        """
        # This method is a placeholder for actual implementation
        # which would involve sending a request to the website and parsing its HTML
        return "Example Website Title"

    @staticmethod
    def calculate_mean(numbers: List[float]) -> float:
        """Calculates the mean of a list of numbers.

        Args:
            numbers (List[float]): The list of numbers.

        Returns:
            float: The mean of the numbers.

        Raises:
            ValueError: If the list is empty.
        """
        if not numbers:
            raise ValueError("Cannot calculate mean of an empty list")
        return sum(numbers) / len(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """Creates a sample DataFrame.

        Returns:
            pd.DataFrame: The sample DataFrame.
        """
        data = {"Name": ["John", "Anna", "Peter"], "Age": [28, 24, 35]}
        return pd.DataFrame(data)

    @staticmethod
    def generate_range(n: int) -> List[int]:
        """Generates a list of squares of numbers from 1 to n.

        Args:
            n (int): The upper limit.

        Returns:
            List[int]: The list of squares.
        """
        return [i ** 2 for i in range(1, n + 1)]

    @staticmethod
    def exception_handling_demo() -> str:
        """Demonstrates exception handling.

        Returns:
            str: A message indicating whether the exception was handled.
        """
        try:
            # This line will raise a ZeroDivisionError
            1 / 0
        except ZeroDivisionError:
            return "Exception handled"
        else:
            return "No exception occurred"


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