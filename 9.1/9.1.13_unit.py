text = input()
counter = 0

for i in range (0, len(text)):
    if (i+1)<len(text):
        if text[i] == text[i+1]:
            counter += 1
    else:
        break

print(counter)