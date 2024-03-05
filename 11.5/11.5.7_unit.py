text = input().split('.')
for i in range(len(text)):
    text[i] = int(text[i])
    if not (0 <= text[i] <= 255):
        print("НЕТ")
        break
else:
    print('ДА')
