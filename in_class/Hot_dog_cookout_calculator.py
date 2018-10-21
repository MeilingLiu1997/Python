people = int(input("Please enter the number of people attending the cookout: "))
hot_dogs = int(input("Please enter the number of hot dogs each person will be given: "))


total = people * hot_dogs

if total % 8 == 0:
    print("The minimum number of packages of hot dogs required: ", total//8)

    print("The minimum number of packages of hot dogs buns required: ", total/8)

    print("The number of hot dogs that will be left over: ", 10 - total % 10)

    print("The number of hot dog buns that will be left over: ", total % 8)
else:
    if total % 10 == 0:
        print("The minimum number of packages of hot dogs required: ", total/10)

        print("The minimum number of packages of hot dogs buns required: ", total/10 + 1)

        print("The number of hot dogs that will be left over: ", total % 10)

        print("The number of hot dog buns that will be left over: ", 8 - total % 8)

    else:
        print("The minimum number of packages of hot dogs required: ", total//10 + 1)

        print("The minimum number of packages of hot dogs buns required: ", total//8 + 1)

        print("The number of hot dogs that will be left over: ", 10 - total % 10)

        print("The number of hot dog buns that will be left over: ", 8 - total % 8)