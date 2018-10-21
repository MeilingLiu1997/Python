def main():
    a = option1()
    b = option2()
    if a < b:
        print("Option 2 is better. Your salary is: $", format(b, '.2f'), sep="")
    else:
        print("Option 1 is better. Your salary is: $", format(a, '.2f'), sep="")

day = 10


def option1():
    base = 100
    total = base * day
    return total


def option2():
    total = (1-2 ** day)/(1-2)
    return total

main()
