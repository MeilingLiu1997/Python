def fact_while(n):
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total


def fact_for(n):
    total = 1
    for i in range(n,0,-1):
        total *= i
    return total


def fact_recursion(n):
    if n == 0:
        return 1
    else:
        n = n * fact_recursion(n-1)
    return n


def main():
    for i in range(1,11):
        print(fact_while(i), fact_for(i), fact_recursion(i))

main()