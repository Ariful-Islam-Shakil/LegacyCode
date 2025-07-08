# testing.py

import pytest
from utils import fetch_website_title, calculate_mean, create_dataframe, count_words, say_hello, generate_range, string_io_example, dictionary_iteration, exception_handling_demo

def test_fetch_website_title():
    url = "https://www.example.com"
    assert fetch_website_title(url) == "No Title Found"

def test_fetch_website_title_with_title():
    url = "https://www.google.com"
    assert fetch_website_title(url) != "No Title Found"

def test_calculate_mean():
    arr = [5, 15, 25]
    assert calculate_mean(arr) == 15.0

def test_calculate_mean_with_empty_list():
    arr = []
    assert calculate_mean(arr) == 0.0

def test_create_dataframe():
    df = create_dataframe()
    assert 'score' in df.columns

def test_create_dataframe_without_score_column():
    df = create_dataframe()
    assert 'score' in df.columns

def test_count_words():
    text = "Python is fun and Python is powerful"
    word_count = count_words(text)
    assert word_count['python'] == 2

def test_count_words_with_empty_text():
    text = ""
    word_count = count_words(text)
    assert len(word_count) == 0

def test_say_hello():
    name = "John"
    greeting = say_hello(name)
    assert greeting == f"Hello, {name}!"

def test_generate_range():
    n = 5
    squares = generate_range(n)
    assert squares == [0, 1, 4, 9, 16]

def test_string_io_example():
    content = string_io_example()
    assert content == "This is a string buffer.\nWorks in Python 3.x with StringIO module.\n"

def test_dictionary_iteration():
    data = {'a': 1, 'b': 2}
    lines = dictionary_iteration(data)
    assert lines == ["a => 1", "b => 2"]

def test_exception_handling_demo():
    error_message = exception_handling_demo()
    assert error_message == "Caught an error: division by zero"

def test_main_function():
    with pytest.raises(SystemExit):
        import main
        main.main()
