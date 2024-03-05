numbers = [int(i) for i in input().split()]
numbers.sort()
print(*numbers, sep=' ')
numbers.sort(reverse=True)
print(*numbers, sep=' ')
