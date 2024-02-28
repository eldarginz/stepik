x = input()
for i in range (0, len(x)):
    if x[i] in '0123456789':
        res = 1
        break
    else:
        res = 0
if res == 1:
    print('Цифра')
if res == 0:
    print('Цифр нет')