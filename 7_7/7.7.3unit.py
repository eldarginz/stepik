count = 0
p = 1
for i in range(0, 10):
    x = int(input())
    if x > -1:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')