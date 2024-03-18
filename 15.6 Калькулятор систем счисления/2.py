n, sis, s = int(input()), 2, ''
while n > 0:
    s = str(n % sis) + s
    n //= sis
print(s)