from typing import Dict, List, Tuple
from dataclasses import dataclass
from io import StringIO
from typing import Any
from typing import Iterator
from typing import TypeVar
from typing import Generic
from typing import TypeAlias
from typing import cast
from typing import Optional
from typing import Union
from typing import Callable
from typing import Sequence
from typing import Iterable

from typing_extensions import TypedDict

T = TypeVar('T')

StringIOBuffer = TypeAlias['StringIO']

class WebsiteTitle(TypedDict):
    title: str

class WordCount(TypedDict):
    word: str
    count: int

class RangeSquares(TypedDict):
    start: int
    end: int
    squares: List[int]

def say_hello(name: str) -> str:
    """
    Prints a greeting message.

    Args:
        name (str): The name to greet.

    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"

def fetch_website_title(url: str) -> str:
    """
    Fetches the title of a website.

    Args:
        url (str): The URL of the website.

    Returns:
        str: The title of the website.
    """
    # Simulate fetching the website title
    return "Example Website Title"

def calculate_mean(numbers: List[float]) -> float:
    """
    Calculates the mean of a list of numbers.

    Args:
        numbers (List[float]): The list of numbers.

    Returns:
        float: The mean of the numbers.
    """
    return sum(numbers) / len(numbers)

def create_dataframe() -> Dict[str, Any]:
    """
    Creates a sample dataframe.

    Returns:
        Dict[str, Any]: The sample dataframe.
    """
    return {"column1": [1, 2, 3], "column2": [4, 5, 6]}

def count_words(text: str) -> WordCount:
    """
    Counts the occurrences of each word in a text.

    Args:
        text (str): The text to count words in.

    Returns:
        WordCount: A dictionary with word counts.
    """
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def generate_range(n: int) -> RangeSquares:
    """
    Generates a range of numbers and calculates their squares.

    Args:
        n (int): The number of elements in the range.

    Returns:
        RangeSquares: A dictionary with the range and its squares.
    """
    start = 0
    end = n
    squares = [i ** 2 for i in range(start, end)]
    return {"start": start, "end": end, "squares": squares}

def string_io_example() -> str:
    """
    Demonstrates the use of StringIO.

    Returns:
        str: The contents of the StringIO buffer.
    """
    buffer = StringIO()
    buffer.write("Hello, World!")
    buffer.seek(0)
    return buffer.read()

def dictionary_iteration() -> Iterator[str]:
    """
    Iterates over a dictionary and yields its keys.

    Yields:
        str: The keys of the dictionary.
    """
    dictionary = {"key1": "value1", "key2": "value2"}
    for key in dictionary:
        yield key

def exception_handling_demo() -> str:
    """
    Demonstrates exception handling.

    Returns:
        str: A message indicating whether an exception was raised.
    """
    try:
        raise Exception("Test exception")
    except Exception as e:
        return f"Exception raised: {e}"
    else:
        return "No exception raised"

def main() -> None:
    """
    The main function.

    Prints various examples and demonstrations.
    """
    print(say_hello("Python 3.12 User"))

    title = fetch_website_title("https://www.example.com")
    print(f"Website Title: {title}")

    mean_val = calculate_mean([5, 15, 25])
    print(f"Mean Value: {mean_val}")

    df = create_dataframe()
    print("DataFrame:")
    for key, value in df.items():
        print(f"{key}: {value}")

    text = "Python is fun and Python is powerful"
    word_count = count_words(text)
    print("Word Counts:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    print("Generated Range Squares:")
    for key, value in generate_range(5).items():
        print(f"{key}: {value}")

    print("StringIO Buffer Output:")
    print(string_io_example())

    print("Dictionary Iteration Output:")
    for line in dictionary_iteration():
        print(line)

    print("Exception Handling Test:")
    print(exception_handling_demo())

if __name__ == '__main__':
    main()