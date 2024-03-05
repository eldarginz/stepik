n = int(input())
numbers = []

for i in range(0, n):
    numbers.append(int(input()))
print(*numbers, sep='\n')
print('')

for i in range(0, n):
    x = numbers[i] * numbers[i] + 2 * numbers[i] + 1
    print(x)
