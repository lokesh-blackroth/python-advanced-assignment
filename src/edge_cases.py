def divide_numbers(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be a number")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be a number")

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


def main():
    print(divide_numbers(10, 2))


if __name__ == "__main__":
    main()