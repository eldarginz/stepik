num = int(input())
cipher = input()

for i in range (0, len(cipher)):
    buffer = ord(cipher[i])
    if buffer - num < 97:
        buffer += 26
    print(chr(buffer-num),end = '')