def divide(a, b):
    return a / b


def parse_and_divide(input_string):
    # Takes "10,2" and returns 5.0
    parts = input_string.split(",")
    return divide(float(parts[0]), float(parts[1]))