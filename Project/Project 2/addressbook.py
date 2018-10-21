import os


def menu():
    print('Choose your option')
    print('1. Add New Contact')
    print('2. Display Address Book')
    print('3. Search for a contact')
    print('4. Modify Contact')
    print('5. Delect Contact')
    print('6. Exit')


def addNew():
    name = input('Name:')
    address = input('Address:')
    phone = input('Phone number:')
    email = input('Email address:')

    old = open('contacts.txt', 'a')
    old.write(name + '\n')
    old.write(address + '\n')
    old.write(phone + '\n')
    old.write(email + '\n')
    print()
    old.close()


def display():
    old = open('contacts.txt','r')

    name = old.readline()
    while name != '':
        address = old.readline()
        phone = old.readline()
        email = old.readline()

        name = name.rstrip('\n')
        address = address.rstrip('\n')
        phone = phone.rstrip('\n')
        email = email.rstrip('\n')

        print('Name:', name)
        print('Address:', address)
        print('Phone:', phone)
        print('Email:', email)
        print()

        name = old.readline()
    old.close()


def search():
    list = []
    namelist = []
    search = input('Search the name of contact:')

    old = open('contacts.txt', 'r')
    name = old.readline()
    while name != '':
        address = old.readline()
        phone = old.readline()
        email = old.readline()
        name = name.rstrip('\n')
        address = address.rstrip('\n')
        phone = phone.rstrip('\n')
        email = email.rstrip('\n')

        x = [name, address, phone, email]
        list.append(x)
        namelist.append(name)
        name = old.readline()

    old.close()

    if search in namelist:
        print(search, 'was found in the list.')
        print(list[namelist.index(search)])
    else:
        print('There is no contact with that name in your address book (capital matters, please double check it).')


def modify():
    list = []
    namelist = []
    modify = input('Whose information needs to be modified?')
    old = open('contacts.txt', 'r')
    new = open('new.txt', 'a')
    name = old.readline()
    while name != '':
        name = name.rstrip('\n')
        address = old.readline()
        phone = old.readline()
        email = old.readline()
        address = address.rstrip('\n')
        phone = phone.rstrip('\n')
        email = email.rstrip('\n')
        x = [name, address, phone, email]
        list.append(x)
        namelist.append(name)
        name = old.readline()

    if modify in namelist:
        print(list[namelist.index(modify)])
        newList = list[namelist.index(modify)]

        while list != '':

            item = input('Which aspect information would you like to modify: '
                         'name, address, phone number, or email address?')

            if item == 'name':
                newName = input('Enter the new name:')
                newList.remove(newList[0])
                newList.insert(0, newName)

                list.remove(newList)
                list.insert(namelist.index(modify), newList)

            elif item == 'address':
                newAddress = input('Enter the new address:')
                newList.remove(newList[1])
                newList.insert(1, newAddress)

                list.remove(newList)
                list.insert(namelist.index(modify), newList)

            elif item == 'phone number':
                newNumber = input('Enter the new number:')
                newList.remove(newList[2])
                newList.insert(2, newNumber)

                list.remove(newList)
                list.insert(namelist.index(modify), newList)

            elif item == 'email address':
                newEmail = input('Enter the new email address:')
                newList.remove(newList[3])
                newList.insert(3, newEmail)

                list.remove(newList)
                list.insert(namelist.index(modify), newList)

            elif item != 'name' or item != 'address' or item != 'phone number' or item != 'email address':
                print('Please input right character.')

            again = input('Back to menu? (y/n)')
            if again == 'y':
                break
    else:
        print('There is no contact with that name in your address book.')

    i = 0
    while i in range(len(list)):
        new.write(list[i][0] + "\n")
        new.write(list[i][1] + "\n")
        new.write(list[i][2] + "\n")
        new.write(list[i][3] + "\n")
        i += 1

    old.close()
    new.close()
    os.remove('contacts.txt')
    os.rename('new.txt','contacts.txt')


def delete():
    list = []
    namelist = []
    delect = input('Enter the name of contact to delete:')
    old = open('contacts.txt', 'r')
    new = open('new.txt', 'a')
    name = old.readline()
    while name != '':
        name = name.rstrip('\n')
        address = old.readline()
        phone = old.readline()
        email = old.readline()
        address = address.rstrip('\n')
        phone = phone.rstrip('\n')
        email = email.rstrip('\n')
        x = [name, address, phone, email]
        list.append(x)
        namelist.append(name)
        name = old.readline()

    if delect in namelist:
        print(list)
        print(list[namelist.index(delect)])
        newList = list[namelist.index(delect)]

        list.remove(newList)
        print(list)

        i = 0
        while i in range(len(list)):
            new.write(list[i][0] + "\n")
            new.write(list[i][1] + "\n")
            new.write(list[i][2] + "\n")
            new.write(list[i][3] + "\n")
            i += 1

        old.close()
        new.close()
    os.remove('contacts.txt')
    os.rename('new.txt', 'contacts.txt')


def exit():
    quit()


def main():
    try:
        print('This is your address book')
        print('=========================')
        choice = 0
        while choice != 6:
            menu()
            choice = int(input('Enter your choice:'))
            if choice == 1:
                addNew()
            elif choice == 2:
                display()
            elif choice == 3:
                search()
            elif choice == 4:
                modify()
            elif choice == 5:
                delete()
            elif choice == 6:
                print('Exit.')
            else:
                print("Invalid choice.")
    except ValueError:
        print('Error: You have to enter interger number. Please try again.')
        print()
        main()
    except IOError:
        print("An error occurred trying to read the file, please re-enter your data again.")
        print()
        main()
    except Exception as err:
        print('There are errors somewhere. Please re-start again.')
        main()
main()