text = input().split()
for i in range(len(text)):
    text[i] = int(text[i])
    print('+'*text[i])