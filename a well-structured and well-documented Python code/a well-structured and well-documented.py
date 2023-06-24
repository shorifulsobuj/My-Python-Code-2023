def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the input number.

    Raises:
        ValueError: If the input number is negative.
    """
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage
try:
    num = int(input("Enter a non-negative integer: "))
    fact = factorial(num)
    print(f"The factorial of {num} is: {fact}")
except ValueError as e:
    print(f"Error: {e}")
