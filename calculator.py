from tabulate import tabulate

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Returns the quotient of two numbers.

    Raises:
        ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def display_results_as_table(a: float, b: float) -> None:
    """
    Displays the results of basic arithmetic operations as a table.

    Args:
        a (float): The first operand.
        b (float): The second operand.
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
    """Performs calculations on two numbers and displays the results."""
    a = 10
    b = 5
    print(f"Performing calculations on {a} and {b}")
    try:
        display_results_as_table(a, b)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()