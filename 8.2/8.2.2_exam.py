n = 8
count = 0
maximum = -10 ** 12

for _ in range(n):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
            
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')