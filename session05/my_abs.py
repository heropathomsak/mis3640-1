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


def f(name):
    print(f'Hi, {name}!')


def main():
    print(my_abs(-1))
    f('Noah')


if __name__ == "__main__":
    main()
