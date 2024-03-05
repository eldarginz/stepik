n = list(input())
n = int(''.join(n[1:]))
text = []

for i in range(n):
    text.append(input())
    if '#' in text[i]:
        text[i] = text[i][0:text[i].find('#')]
    text[i] = text[i].rstrip()

print(*text, sep='\n')
