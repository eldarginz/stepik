num = int(input())
output = []

for i in range(num, 0, -1):
    if num % i == 0:
        output.append(i)

print(output[::-1])
