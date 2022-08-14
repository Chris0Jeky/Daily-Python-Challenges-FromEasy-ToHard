print("ciao")


def divide_or_square(num):
    check1 = num / 5
    check2 = num // 5
    if (check1 - check2) == 0:
        return print(str(pow(num, 0.5)))
    else:
        return print(str(num % 5))

divide_or_square(6)