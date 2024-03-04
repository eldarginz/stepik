def numbertudasuda(n):
    count = n // 2

    # часть 1
    for i in range(count):
        print(i + 1, end='')

    # центр
    print(count + 1, end='')

    # часть 2
    for i in range(count, 0, -1):
        print(i, end='')


s = int(input())
counter = 1

for i in range(s):
    numbertudasuda(counter)
    counter +=2
    print('')