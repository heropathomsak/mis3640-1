def calc(x):
    result = 0
    for i in range(x + 1):
        # print(i, result)
        result += i
    return result


def main():
    y = 10
    myresult = calc(5)  # my intention was to sum up from 1 to 5
    print(myresult)


if __name__ == "__main__":
    main()
