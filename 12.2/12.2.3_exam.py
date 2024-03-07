a = input().split()

result = 0

for i in range(len(a)):
    result += int(a[i])

print(*a, sep='+', end='=')
print(result)
