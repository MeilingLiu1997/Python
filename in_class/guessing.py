import random
number = random.randint(1, 20)
restart = "y"
count = 5
guess_number = int(input("You have 5 changes to guess number (between 1 to 20): "))

while restart == "y":
    while count > 1:
        if guess_number < number:
            count = count - 1
            print("This guess is too low!")
            print("Your remaining:",count,"time(s).")
            guess_number = int(input("You have 5 changes to guess number (between 1 to 20): "))
        elif guess_number > number:
            count = count - 1
            print("This guess is too high!")
            print("Your remaining:",count,"time(s).")
            guess_number = int(input("You have 5 changes to guess number (between 1 to 20): "))
        elif guess_number == number:
            count = count - 1
            print("This is correct!")
            print("The answer is:", number)
            restart = input("Do you want to try new one?(y/n): ")
            if restart == "n":
                print("Quit.")
            else:
                guess_number = int(input("You have 5 changes to guess number (between 1 to 20): "))
                count = 5
                import random
                number = random.randint(1, 20)
    print("Sorry you didn't guess the number.\n The number was:", number)
    restart = input("Do you want to try new one?(y/n): ")
    if restart == "n":
        print("Quit.")
    else:
        guess_number = int(input("You have 5 changes to guess number (between 1 to 20): "))
        count = 5
        import random
        number = random.randint(1, 20)