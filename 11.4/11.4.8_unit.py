minus = []
zero = []
plus = []

for i in range(int(input())):
    buffer = int(input())
    if buffer == 0:
        zero.append(buffer)
    if buffer < 0:
        minus.append(buffer)
    if buffer > 0:
        plus.append(buffer)

print(*minus, *zero, *plus, sep='\n')
