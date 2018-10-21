name = {'Meiling Liu': 'April 2', 'Tracy': 'March 15', 'Kai': 'November 15', 'Paulina':'June 18'}


def display():
    print('Your dictionary')
    print('=================')
    for key, value in name.items():
        print(key, value)

ask = input('Enter a full name (type "quit" for quit):')
count = 0
while count >= 0:
    if ask in name:
        print(name[ask])
        ask = input('Enter a full name (type "quit" for quit):')

    elif ask == 'quit' or ask == 'Quit':
        quit()
    else:
        create = input("Want to create a new person's birthday? (y or n):")
        if create == 'y' or create == 'Y':
            birthday = input('Please add a new birthday:')
            name[ask] = birthday
            display()
            ask = input('Enter a full name (type "quit" for quit):')
        elif create == 'n' or create == 'N':
            ask = input('Enter a full name (type "quit" for quit):')