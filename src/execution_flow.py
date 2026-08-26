def calculate_total(price, quantity):
    total = price * quantity
    return total


def create_order(product, price, quantity):
    total = calculate_total(price, quantity)

    return {
        "product": product,
        "quantity": quantity,
        "total": total,
    }


def main():
    order = create_order("Laptop", 50000, 2)
    print(order)


if __name__ == "__main__":
    main()