a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4 * a * c

if d == 0:
    print(-b/(2*a))
elif d>0:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    print(min(x1,x2))
    print(max(x1,x2))
elif d<0:
    print('Нет корней')