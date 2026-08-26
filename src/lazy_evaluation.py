def generate_numbers(limit):
    for number in range(1, limit + 1):
        yield number


def main():
    numbers = generate_numbers(5)

    print("Generator created")

    for number in numbers:
        print("Value:", number)


if __name__ == "__main__":
    main()