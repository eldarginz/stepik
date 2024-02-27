x = int(input())
xlast = x % 10
xfirst = int(0)
xcounter = int(0)
xsumma = int(0)
xproiz = int(1)

while x > 99:
    xcounter += 1
    xsumma += x % 10
    xproiz *= x % 10
    if x > 0:
        xfirst = x
    x //= 10


print(xfirst%10)