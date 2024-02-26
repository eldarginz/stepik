n = int(input())
while n > 9:
    last_dig = n % 10
    n = n // 10
print(n)