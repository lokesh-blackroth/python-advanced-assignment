def create_greeting(name):
    def greet():
        print("Hello", name)

    return greet


def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def main():
    hello_lokesh = create_greeting("Lokesh")
    hello_lokesh()

    counter = create_counter()

    print(counter())
    print(counter())
    print(counter())


if __name__ == "__main__":
    main()