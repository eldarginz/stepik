num = int(input())
numbers = []

for i in range(0, num):
    numbers.append(int(input()))

del numbers[1::2]

print(numbers)
