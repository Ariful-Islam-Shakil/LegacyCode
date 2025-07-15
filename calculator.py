from tabulate import tabulate
from typing import List, Tuple

def add(a: float, b: float) -> float:
    """Performs addition of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.

    Raises:
        TypeError: If a or b is not a number.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """Performs subtraction of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference of a and b.

    Raises:
        TypeError: If a or b is not a number.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """Performs multiplication of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.

    Raises:
        TypeError: If a or b is not a number.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """Performs division of two numbers.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient of a and b.

    Raises:
        ValueError: If b is zero.
        TypeError: If a or b is not a number.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def display_results_as_table(a: float, b: float) -> None:
    """Displays the results of arithmetic operations as a table.

    Args:
        a (float): The first number.
        b (float): The second number.
    """
    results = [
        ["Operation", "Result"],
        ["Addition", add(a, b)],
        ["Subtraction", subtract(a, b)],
        ["Multiplication", multiply(a, b)],
        ["Division", divide(a, b)]
    ]
    print(tabulate(results, headers="firstrow", tablefmt="grid"))

def main() -> None:
    """Runs the main program."""
    a: float = 10
    b: float = 5
    print(f"Performing calculations on {a} and {b}")
    try:
        display_results_as_table(a, b)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()