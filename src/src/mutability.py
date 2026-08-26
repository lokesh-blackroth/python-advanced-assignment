def immutable_example():
    number = 10

    print("Before:", number)
    print("Before ID:", id(number))

    number = 20

    print("After:", number)
    print("After ID:", id(number))


def mutable_example():
    numbers = [1, 2, 3]

    print("Before:", numbers)
    print("Before ID:", id(numbers))

    numbers.append(4)

    print("After:", numbers)
    print("After ID:", id(numbers))


if __name__ == "__main__":
    immutable_example()
    print()
    mutable_example()