num = input()
num = num[::-1]

itog = 0

for i in range(len(num)):
    print(i, '', num[i])
    itog += int(num[i]) * 2 ** i

print('---', itog)