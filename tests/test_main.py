```python
# tests/test_main.py

import pytest
from main import StringUtils, MathUtils
from io import StringIO
import pandas as pd
import numpy as np

def test_say_hello():
    assert StringUtils.say_hello("John") == "Hello, John!"

def test_count_words():
    text = "This is a test text"
    word_count = StringUtils.count_words(text)
    assert word_count == {'this': 1, 'is': 1, 'a': 1, 'test': 1, 'text': 1}

def test_string_io_example():
    buffer = StringIO()
    buffer.write("Hello, World!")
    buffer.seek(0)
    assert StringUtils.string_io_example() == "Hello, World!"

def test_dictionary_iteration():
    expected_output = ["key1: value1", "key2: value2"]
    assert StringUtils.dictionary_iteration() == expected_output

def test_fetch_website_title():
    url = "https://www.example.com"
    assert MathUtils.fetch_website_title(url) == "www.example.com"

def test_calculate_mean():
    numbers = [5, 15, 25]
    assert MathUtils.calculate_mean(numbers) == 15.0

def test_create_dataframe():
    expected_df = pd.DataFrame({"Name": ["John", "Mary", "David"], "Age": [25, 31, 42]})
    assert MathUtils.create_dataframe().equals(expected_df)

def test_generate_range():
    expected_output = [1, 4, 9, 16, 25]
    assert MathUtils.generate_range(5) == expected_output

def test_exception_handling_demo():
    assert MathUtils.exception_handling_demo() == "Exception handled"

def test_main():
    # Test the main function
    # This test is not as straightforward as the others, but it's still useful
    # to ensure that the main function doesn't raise any exceptions
    try:
        main()
    except Exception as e:
        pytest.fail(f"Main function raised an exception: {e}")

def test_main_prints_hello_message(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, Python 3.12 User!" in captured.out

def test_main_prints_website_title(capsys):
    main()
    captured = capsys.readouterr()
    assert "Website Title: www.example.com" in captured.out

def test_main_prints_mean_value(capsys):
    main()
    captured = capsys.readouterr()
    assert "Mean Value: 15.0" in captured.out

def test_main_prints_dataframe(capsys):
    main()
    captured = capsys.readouterr()
    assert "DataFrame:" in captured.out

def test_main_prints_word_counts(capsys):
    main()
    captured = capsys.readouterr()
    assert "Word Counts:" in captured.out

def test_main_prints_generated_range_squares(capsys):
    main()
    captured = capsys.readouterr()
    assert "Generated Range Squares:" in captured.out

def test_main_prints_string_io_buffer_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "StringIO Buffer Output:" in captured.out

def test_main_prints_dictionary_iteration_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Dictionary Iteration Output:" in captured.out

def test_main_prints_exception_handling_test(capsys):
    main()
    captured = capsys.readouterr()
    assert "Exception Handling Test: Exception handled" in captured.out
```