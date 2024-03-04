num = int(input())
text = []

for i in range(0, num):
    text.append(input())

symbol = int(input())

for i in range(0, num):
    if len(text[i]) >= symbol:
        buffer = text[i]
        print(buffer[symbol-1], end='')
