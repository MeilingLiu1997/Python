# method 1: make a new list, then copy the original list into the new list backwords.
# newList = [] + l # make a copy or copy this way: newList = [0] + len(1)

def reverseList_copy(list):
    newList = []
    i = len(list) - 1
    while i >= 0:
        newList.append(list[i])
        i -= 1
    return newList

# method 2:take the original list (no copy) ,swap 1st & last element, swap the 2nd and 2nd to last element...
def reverseList_inPlace(list):
    i = 0
    length = len(list) // 2
    while i < length:
        temp = list[i]
        list[i] = list[-(i+1)]
        list[-(i+1)] = temp
        i += 1
    return list


def main():
    l = [4,3,2,1]
    m = ['Crush','Mr. Incredible', 'Bing Bong', 'Buzz']
    n = ['Awesome', 2130, 'is', 54, 'CS110', 1.345]
    print('Original list 1:', l)
    print('Reversed list 1:', reverseList_copy(l))
    print('Original list 2:', m)
    print('Reversed list 2:', reverseList_inPlace(m))
    print('Original list 3:', n)
    print('Reversed list 3:', reverseList_copy(n))
main()