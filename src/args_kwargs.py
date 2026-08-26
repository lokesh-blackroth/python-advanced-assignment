def add_numbers(*args):
    return sum(args)


def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def main():
    total = add_numbers(10, 20, 30, 40)
    print("Total:", total)

    show_details(
        name="Lokesh",
        role="Software Engineer",
        experience="Fresher",
    )


if __name__ == "__main__":
    main()