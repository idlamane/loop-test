def divide(a, b):
    return a / b


def parse_and_divide(input_string):
    """Parse two comma-separated numbers and return their quotient.

    Raises ValueError for malformed input or division by zero.
    """
    parts = input_string.split(",")
    if len(parts) != 2:
        raise ValueError("Input must contain exactly two comma-separated numbers")

    try:
        a = float(parts[0])
        b = float(parts[1])
    except ValueError:
        raise ValueError("Both parts must be valid numbers")

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return divide(a, b)


def parse_and_multiply(input_string):
    """Parse two comma-separated numbers and return their product.

    Raises ValueError for malformed input or non-numeric values.
    """
    parts = input_string.split(",")
    if len(parts) != 2:
        raise ValueError("Input must contain exactly two comma-separated numbers")

    try:
        a = float(parts[0])
        b = float(parts[1])
    except ValueError:
        raise ValueError("Both parts must be valid numbers")

    return a * b
