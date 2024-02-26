num = int(input())

for i in range(num):
    x = i+1
    if 5 <= x <= 9:
        continue
    else:
        if 17 <= x <= 37:
            continue
        else:
            if 78 <= x <= 87:
                continue
            else:
                print(i+1)