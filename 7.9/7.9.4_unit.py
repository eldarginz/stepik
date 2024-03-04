def findDevNum(n):
    i = 2
    degree = 0
    result = 1
    while n >= 1:
        if n%i == 0:
            degree += 1
            n = n // i
        else:
            result *= (degree+1)
            degree = 0
            i += 1
            if n == 1: return result

def printzvezdochki(n):
    for i in range (1, n+1):
        print('+',end='')

n = int(input())

for i in range (1, n+1):
    print(i, end='')
    printzvezdochki(findDevNum(i))
    print('')