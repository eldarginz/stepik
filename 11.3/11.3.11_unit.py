n = int(input())
numbers = []
result = []

for i in range(1, n+1):
    numbers.append(int(input()))

for i in range(0, len(numbers)):
    if i+1 != len(numbers):
        result.append(numbers[i]+numbers[i+1])
    else:
        break

print(result)
