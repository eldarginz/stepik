def factorial(n):
    counter = int(1)
    for i in range(1, n + 1):
        counter *= i
    return counter


x = int(input())
result = 0

for i in range(1, x + 1):
    result = result + factorial(i)

print(result)
