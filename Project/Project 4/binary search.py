list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
target = 15


def binary_search(target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high)/2)
        if target == list[mid]:
            return mid
        elif target < list[mid]:
            high = mid-1
            return high
        else:
            low = mid+1
            return low
    return -1


def main():
    print(binary_search(target))
main()