def calculate_average(numbers):
    if not numbers:
        return 0

    total = sum(numbers)
    count = len(numbers)

    return total / count


def main():
    numbers = [10, 20, 30, 40, 50]

    average = calculate_average(numbers)

    print("Average:", average)


if __name__ == "__main__":
    main()