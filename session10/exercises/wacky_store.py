def get_price(item):
    """
    calculate the price of item according to the letters in its name, and return the price

    item: a string
    """
    price = 0
    for letter in item:
        if letter.isalpha():
            price += ord(letter) - 96
    return price


# print(get_price('bananas'))
# print(get_price('potato chips'))


def print_receipt(items):
    """
    prints the receipt of items and prices nicely

    items: a list of strings 
    """
    total_price = 0
    longest_word = max(items, key=len)
    width = len(longest_word)
    for item in items:
        price = get_price(item)
        print(
            "{:<{number_length}}  ${:>6,.2f}".format(item, price, number_length=width)
        )
        total_price += price

    print("-" * (width + 9))
    print(
        "{:<{number_length}}  ${:>6,.2f}".format(
            "Total", total_price, number_length=width
        )
    )


def main():
    items = ["bananas", "rice", "paprika", "potato chips"]
    print_receipt(items[:])


if __name__ == "__main__":
    main()
