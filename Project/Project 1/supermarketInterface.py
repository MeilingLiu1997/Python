# 95/100: losing points on: need display cost of each items and new total, missing cost of each items that users want to buy.


print("Welcome to the CS110 Supermarket!")
print('=================================')

total = 0
choice = 0

while choice != 5:
    print("1. Potatoes ($0.75 per potato)")
    print("2. Tomatoes ($1.25 per tomato)")
    print("3. Apples   ($0.50 per apple)")
    print("4. Mangoes  ($1.75 per mango)")
    print("5. Check out.")

    choice = float(input("Please enter your choice (from 1 to 4): "))

    if choice == 1:
        number = float(input('How many potato(es)?'))
        while number < 0 or number != int(number):
            print('Invalid enter.')
            number = float(input('How many potato(es)?'))
        total = number * 0.75 + total

    elif choice == 2:
        number = float(input('How many tomato(es)?'))
        while number < 0 or number != int(number):
            print('Invalid enter.')
            number = float(input('How many tomato(es)?'))
        total = number * 1.25 + total

    elif choice == 3:
        number = float(input('How many apple(es)?'))
        while number < 0 or number != int(number):
            print('Invalid enter.')
            number = float(input('How many apple(es)?'))
        total = number * 0.50 + total

    elif choice == 4:
        number = float(input('How many mango(es)?'))
        while number < 0 or number != int(number):
            print('Invalid enter.')
            number = float(input('How many mango(es)?'))
        total = number * 1.75 + total

    elif choice == 5:
        print("Check out. Here is your total: $", total, sep="")
        amount = float(input('Please enter an amount to pay: '))

        while amount < 0 or amount < total:
            print('You need to put more money.')
            amount = float(input('Please enter an amount to pay: '))

        change = amount - total
        print("Change is:",change)
        number_5 = int(change//5)
        number_1 = int((change-5*number_5)//1)
        number_quarters = int((change-5*number_5-number_1)/0.25)
        number_dimes = int((change-5*number_5-number_1-0.25*number_quarters)//0.1)
        number_nickels = int((change-5*number_5-number_1-0.25*number_quarters-0.1*number_dimes)//0.05)
        number_pennies=int((change-5*number_5-number_1-0.25*number_quarters-0.1*number_dimes-0.05*number_nickels)//0.01)

        print("Give the customer: ")
        if number_5 > 0:
            print(number_5, "$5 note", "and", end=" ")
        if number_1 > 0:
            print(number_1, "$1", "and", end=" ")
        if number_quarters > 0:
            print( number_quarters,"quarter(s)","and", end=" ")
        if number_dimes > 0:
            print(number_dimes, "dime(s)", "and", end=" ")
        if number_nickels > 0:
            print(number_nickels, "nickel(s)", "and", end=" ")
        if number_pennies > 0:
            print(number_pennies, "penny(ies)")

    else:
        print('Invalid enter.')
    print("Your've purchased: $",total, sep="")
