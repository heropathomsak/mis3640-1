def f():
    print('Hi')
    f()


def countdown(n):
    import time

    time.sleep(1)

    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n)


# countdown(5)


# fibonacci series: 1, 1, 2, 3, 5, 8, 13 ...


def fibonacci(n):
    """
    returns the n-th fibonacci number
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(1))
# 1
print(fibonacci(2))
# 1
print(fibonacci(3))
# 2
print(fibonacci(4))
# 3
print(fibonacci(5))
# 5
print(fibonacci(6))
# 8
print(fibonacci(7))
# fibonacci(5) + fibonacci(6) -> 13
