num = [i for i in input().split('-')]
num2 = ''.join(num)

if num2.isdigit():
    if (int(num[0]) == 7 and len(num[1]) == 3 and len(num[2]) == 3 and len(num[3]) == 4) or (len(num[0]) == 3 and len(num[1]) == 3 and len(num[2]) == 4):
        print('YES')
    else:
        print('NO')
else:
    print('NO')
    quit()
