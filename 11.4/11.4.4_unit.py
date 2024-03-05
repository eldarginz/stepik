n = int(input())
numbers = []

for i in range(0, n):
    numbers.append(int(input()))

numbers.remove(max(numbers))
numbers.remove(min(numbers))

print(*numbers, sep='\n')
