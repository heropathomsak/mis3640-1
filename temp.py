def f(a, b, c):
    return a + b + c, a * b * c


# result_one, result_two = f(2, 3, 4)
# print(result_one)
# print(result_two)


def f2():
    """this function will change the world"""
    print('Hi')
    return None


# result = f2()
# print(result)


# today = 'Thursday'
# if today == 'Thursday':
#     pass


def my_abs(x):
    """"""
    # First, check the type of x
    # if x is an integer, or a float, move to the next step
    #    if x is negative,  return the opposite value of x
    #    else, just return x
    # if not, do something
    if isinstance(x, int) or isinstance(x, float):
        if x < 0:
            return -x
        else:
            return x
    else:
        print('x is not a number!')


def my_abs2(x):
    """returns the abosolute value of x
    x: an integer or a float"""
    