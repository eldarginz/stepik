a = input().split()
b = input().split()

print(*[int(a[i])+int(b[i]) for i in range(len(a))])
