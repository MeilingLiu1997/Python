1import dog
import cat
import fish
import bird
import csv
name_list = []


def main():
    try:
        with open('pets.csv', 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)
            for i in range(0, len(your_list)):
                if your_list[i][0] == 'Dog':
                    d = dog.Dog(your_list[i][1], your_list[i][2], your_list[i][3],your_list[i][4])
                    name_list.append(d.name)
                elif your_list[i][0] == 'Cat':
                    c = cat.Cat(your_list[i][1], your_list[i][2], your_list[i][3], your_list[i][4])
                    name_list.append(c.name)
                elif your_list[i][0] == 'Fish':
                    f = fish.Fish(your_list[i][1], your_list[i][2], your_list[i][3], your_list[i][4])
                    name_list.append(f.name)
                elif your_list[i][0] == 'Bird':
                    b = bird.Bird(your_list[i][1], your_list[i][2], your_list[i][3], your_list[i][4])
                    name_list.append(b.name)


        # Show only pets of a certain type # Based on the user input, show only the pets that are dogs/cats/fish/birds.
        def animal_type(enter):
            for i in range(0, len(your_list)):
                if your_list[i][0] == enter.title():
                    print('-', your_list[i][3])
            return ''


        # Search for a Pet -
        # you will call your own binary search function to search for the first pet name that matches the user entered string.
        # If a pet is found in the list, then print all the details for that pet and the index in the list where it was found.
        # If the pet is not in the list, then print a message informing the user that the pet is not in the list.
        def search(enter):
            low = 0
            high = len(your_list)-1
            insertion_sort_name(your_list)
            while low <= high:
                mid = int((low + high) / 2)
                if ' ' + enter.title() == your_list[mid][1]:
                    print("The index is " + str(mid) + " in the list.")
                    return your_list[mid]
                elif ' ' + enter.title() < str(your_list[mid][1]):
                    high = mid - 1
                else:  # enter > your_list[mid]
                    low = mid + 1
            return 'The pet is not in the list.'


        # Sort list based on pet name -
        # For all the sort options you can implement either selection sort or insertion sort on the list of pet objects.
        # After sorting the list, display the sorted list.
        def insertion_sort_name(list):
            keyIndex = 1
            while keyIndex < len(list):
                insert_nameorder(list, keyIndex)
                keyIndex += 1

        def insert_nameorder(list, keyIndex):
            key = list[keyIndex][1]
            j = keyIndex -1
            while (list[j][1] >= key) and (j >= 0):
                list[j + 1][1] = list[j][1]
                j -= 1
                list[j + 1][1] = key


        # Sort list based on pet color - After sorting the list, display the sorted list.
        def insertion_sort_color(list):
            keyIndex = 1
            while keyIndex < len(list):
                insert_colororder(list, keyIndex)
                keyIndex += 1

        def insert_colororder(list, keyIndex):
            key = list[keyIndex][4]
            j = keyIndex - 1
            while (list[j][4] >= key) and (j >= 0):
                list[j + 1][4] = list[j][4]
                j -= 1
                list[j + 1][4] = key

        print('Your Pet Finder menu: ')
        print('===========================')
        enter1 = 0
        while enter1 != 6:
            print('1. Display the names of all the pets.')
            print('2. Certain types of pets.')
            print('3. Search for a Pet.')
            print('4. Sort list based on pet name.')
            print('5. Sort list based on pet color.')
            print('6. Exit the program.')

            enter1 = float(input('Enter your choice: '))
            if enter1 == 1:
                # Print only the names of all the pets
                print('Here are the names of pets:')
                print(name_list)
                print('')
            elif enter1 == 2:
                enter2 = input('What kind of pet would you like to see (dog/cat/fish/bird): ')
                print(animal_type(enter2))
            elif enter1 == 3:
                enter3 = input('Search pet name: ')
                print(search(enter3))
                print('')
            elif enter1 == 4:
                insertion_sort_name(your_list)
                print('Sorted list: ', your_list)
                print('')
            elif enter1 == 5:
                insertion_sort_color(your_list)
                print('Sorted list: ', your_list)
                print('')
            elif enter1 == 6:
                exit()
            else:
                print('Invalid value.')
    except IOError:
        print('An error occurred trying to read')
        print('Non-numeric data is allowed.')
        print('Your Pet Finder menu: ')
        print('===========================')
        print('1. Display the names of all the pets.')
        print('2. Certain types of pets.')
        print('3. Search for a Pet.')
        print('4. Sort list based on pet name.')
        print('5. Sort list based on pet color.')
        print('6. Exit the program.')
        enter1 = float(input('Enter your choice: '))
    except ValueError:
        print('Non-numeric data is allowed.')
        print('Your Pet Finder menu: ')
        print('===========================')
        print('1. Display the names of all the pets.')
        print('2. Certain types of pets.')
        print('3. Search for a Pet.')
        print('4. Sort list based on pet name.')
        print('5. Sort list based on pet color.')
        print('6. Exit the program.')
        enter1 = float(input('Enter your choice: '))
    except Exception as err:
        print(err)
        print('Non-numeric data is allowed.')
        print('Your Pet Finder menu: ')
        print('===========================')
        print('1. Display the names of all the pets.')
        print('2. Certain types of pets.')
        print('3. Search for a Pet.')
        print('4. Sort list based on pet name.')
        print('5. Sort list based on pet color.')
        print('6. Exit the program.')
        enter1 = float(input('Enter your choice: '))
main()
