import utils.string_utils as string_utils
import utils.math_utils as math_utils
from typing import Dict

def main() -> None:
    """Main function to demonstrate utility functions."""
    print(string_utils.say_hello("Python3.12 User"))

    title = math_utils.fetch_website_title("https://www.example.com")
    print(f"Website Title: {title}")

    mean_val = math_utils.calculate_mean([5, 15, 25])
    print(f"Mean Value: {mean_val}")

    df = math_utils.create_dataframe()
    print("DataFrame:\n", df)

    text = "Python is fun and Python is powerful"
    word_count: Dict[str, int] = string_utils.count_words(text)
    print("Word Counts:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

    print("Generated Range Squares:", math_utils.generate_range(5))

    print("StringIO Buffer Output:\n" + string_utils.string_io_example())

    print("Dictionary Iteration Output:")
    for line in string_utils.dictionary_iteration():
        print(line)

    print("Exception Handling Test:", math_utils.exception_handling_demo())

if __name__ == '__main__':
    main()