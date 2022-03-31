def get_invoice_items(items):
    invoice_items = []
    for item in items:
        subtotal = item["price"] * item["quantity"]
        name = item["name"]
        quantity = item["quantity"]
        invoice_items.append(f"{quantity} {name}  {subtotal} KD")
    return invoice_items


def get_total(items):
    total = 0
    for item in items:
        itemSubtotal = item["price"] * item["quantity"]
        total += itemSubtotal
    return total


def print_receipt(invoice_items, total):
    print("Here's you receipt sir 👨🏼‍🍳")
    print("-" * 20)
    print(*invoice_items, sep="\n")
    print("-" * 20)
    print(total)


def main():
    items = []
    item_name = input("Enter an item : ")

    while item_name != "done":
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        items.append({"name": item_name, "price": price, "quantity": quantity})

        item_name = input("Item (enter 'done' when finished): ")

    invoice_items = get_invoice_items(items)
    total = get_total(items)
    print_receipt(invoice_items, total)


if __name__ == "__main__":
    main()
