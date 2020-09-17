def my_abs(number):
    """
    number: an integer or a floating number
    return the absolute value of a number
    """
    if isinstance(number, (int, float)):
        if number >= 0:
            return number
        else:
            return -number
    else:
        print('I don\'t know how to solve this')


# print(my_abs(-1))

def main():
    print(my_abs(-1))


if __name__ == "__main__":
    main()
