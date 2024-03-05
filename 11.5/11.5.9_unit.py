text = input().split()
for i in range(len(text)):
    text[i] = int(text[i])
count = 0

for i in range(len(text)):
    for j in range(i+1, len(text)):
        if text[i] == text[j]:
            count += 1

print(count)
