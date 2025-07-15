import string
import math
import pandas as pd
from typing import Dict, List, Tuple, Optional

class StringUtils:
    """String utility class."""
    
    @staticmethod
    def say_hello(name: str) -> str:
        """Prints a greeting message with the given name."""
        
        return f"Hello, {name}!"

    @staticmethod
    def count_words(text: str) -> Dict[str, int]:
        """Counts the occurrences of each word in the given text."""
        
        words = text.split()
        word_count: Dict[str, int] = {}
        
        for word in words:
            word = word.lower()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        return word_count

    @staticmethod
    def string_io_example() -> str:
        """Demonstrates using StringIO for string output."""
        
        from io import StringIO
        buffer = StringIO()
        buffer.write("Hello, World!")
        buffer.seek(0)
        return buffer.read()

    @staticmethod
    def dictionary_iteration() -> List[str]:
        """Iterates over a dictionary and returns its keys."""
        
        dictionary = {"key1": "value1", "key2": "value2"}
        return list(dictionary.keys())


class MathUtils:
    """Math utility class."""
    
    @staticmethod
    def fetch_website_title(url: str) -> Optional[str]:
        """Fetches the title of the given website (not implemented)."""
        
        # This method is not implemented as it requires a web scraping library.
        # For demonstration purposes, it returns None.
        return None

    @staticmethod
    def calculate_mean(numbers: List[float]) -> float:
        """Calculates the mean of the given list of numbers."""
        
        return sum(numbers) / len(numbers)

    @staticmethod
    def create_dataframe() -> pd.DataFrame:
        """Creates a sample DataFrame (not implemented)."""
        
        # This method is not implemented as it requires a DataFrame.
        # For demonstration purposes, it returns an empty DataFrame.
        return pd.DataFrame()

    @staticmethod
    def generate_range(n: int) -> List[int]:
        """Generates a list of squares from 0 to n."""
        
        return [i ** 2 for i in range(n + 1)]

    @staticmethod
    def exception_handling_demo() -> str:
        """Demonstrates exception handling."""
        
        try:
            raise ValueError("Test exception")
        except ValueError as e:
            return f"Caught exception: {e}"


def main() -> None:
    """Main function."""
    
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