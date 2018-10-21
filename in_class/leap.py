year = int(input("Please enter the year that you want to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        print("This year is not a leap year!")
    else:
        print("This year is a leap year!")
else:
    print("This year is not a leap year!")

