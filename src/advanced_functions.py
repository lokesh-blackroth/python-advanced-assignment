def square(number):
    return number * number


def double(number):
    return number * 2


def apply_operation(operation, number):
    return operation(number)


def main():
    square_result = apply_operation(square, 5)
    double_result = apply_operation(double, 5)

    print("Square:", square_result)
    print("Double:", double_result)


if __name__ == "__main__":
    main()