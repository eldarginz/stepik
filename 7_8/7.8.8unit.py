n = int(input())
count = n//2

# часть 1
for i in range(count):
    for j in range(i+1):
        print('*', end='')
    print('')

# центр
for j in range(count+1):
    print('*', end='')
print('')

# часть 2
for i in range(count, 0, -1):
    for j in range(i):
        print('*', end='')
    print('')