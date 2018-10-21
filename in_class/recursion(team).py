def printing(n):
    if n > 0:
        printing(n-1)
        print(n)
    return n

def multiplication(x,y):
    if x == 0:
        return 0
    else:
        return y + multiplication(x-1, y)
    return n

def asterisks(n):
    if (n > 1):
        asterisks(n - 1)
    print("*" * n)
    return n

def largestList(list):
    if len(list) == 1:
        return list[0]
    else:
        m = largestList(list[1:])
        if m > list[0]:
            return m
        else:
            return list[0]

def listSum(list):
   if len(list) == 1:
        return list[0]
   else:
        return list[0] + listSum(list[1:])

def numSum(n):
    if n < 1:
        return n
    else:
        return n + numSum(n - 1)

def power(x,y):
    if y == 1:
        return x
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

def main():
    printing(5)
    print('=========================')
    print(multiplication(4,7))
    print('=========================')
    asterisks(6)
    print('=========================')
    list = [123,3242,45154351,-12314,156,0]
    print(largestList(list))
    print('=========================')
    print(listSum(list))
    print('=========================')
    print(numSum(50))
    print('=========================')
    print(power(4,2))
main()