n = int(input())
text = []
text_low = []

for i in range(0, n):
    text.append(input())

search = input()

for i in range(0, n):
    text_low.append(text[i].lower())
    if search.lower() in text_low[i]:
        print(text[i])
