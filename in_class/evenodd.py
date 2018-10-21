def main():
    n = int(input("Please enter an integer number: "))
    iseven(n)


def iseven(n):
    if n % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")
main()