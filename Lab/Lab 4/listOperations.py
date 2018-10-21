
def findLowest(listName):
    min_num = None
    for min in listName:
        if min_num == None:
            min_num = min
        elif min_num > min:
            min_num = min
    return min_num


def findHighest(listName):
    max_num = None
    for max in listName:
        if max_num == None:
            max_num = max
        elif max > max_num:
            max_num = max
    return max_num


def computeTotal(listName):
    total = 0
    for value in listName:
        total += value
    return total


def computeAverage(listName):
    total = 0
    for value in listName:
        total += value
    average = total / len(listName)
    return average

def printAlternate(listName):
    newList = []
    for x in range(0, 5):
        num = listName[2 * x + 1]
        newList.append(num)
    return newList

def main():
    listName = []
    for count in range(10):
        listName.append(int(input('Please enter a series of 10 numbers: ')))
    print('The lowest number in the list is:',findLowest(listName))
    print('The hightest number in the list is:',findHighest(listName))
    print('The total of all the numbers is:', computeTotal(listName))
    print('The average of all the numbers is:', computeAverage(listName))
    print('The alternate numbers:',printAlternate(listName))
main()
