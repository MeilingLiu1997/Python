print("Welcome to CS110-04 ATM machine")
print('===============================')

balance = 1500.00
transactionChoice = 0

while transactionChoice != 4:
    print('Choose your option')
    print('1. Deposit funds')
    print('2. Withdraw funds')
    print('3. See balance')
    print('4. Quit')

    transactionChoice = int(input("Enter a number 1-4: "))

    if transactionChoice == 1: #Deposit funds
        deposit = float(input("Put in the money. How much?"))
        balance += deposit
    elif transactionChoice == 2: #Withdraw funds
        withdraw = float(input("How much? "))
        while withdraw < 0 or withdraw > balance:
            print("This is not a valid withdrawal amount.")
            withdraw = float(input("How much? "))
        balance -= withdraw
    elif transactionChoice == 3: #See balance
        print("Balance is", balance)
    elif transactionChoice == 4: #Quit
        print("See you later!")
    else:
        print("Invalid choice.")
    print("New balance: ", balance)