def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])


def main():
    people = [
        ("Lokesh", 25),
        ("Rahul", 22),
        ("Arun", 28),
    ]

    result = sort_by_age(people)

    print(result)


if __name__ == "__main__":
    main()