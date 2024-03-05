n = int(input())
a = []
b = []
c = []

for i in range(n):
    a.append(input())

k = int(input())

for j in range(k):
    b.append(input())

for h in range(len(a)):
    count = 0
    for g in range(len(b)):
        if b[g].lower() in a[h].lower():
            count += 1
        if count == len(b):
            c.append(a[h])

print(*c, sep='\n')