def iterator_example():
    numbers = [10, 20, 30]

    iterator = iter(numbers)

    print("Iterator:")
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))


def generator_example():
    print("Generator:")

    for number in generate_numbers():
        print(number)


def generate_numbers():
    yield 10
    yield 20
    yield 30


def main():
    iterator_example()
    print()
    generator_example()


if __name__ == "__main__":
    main()