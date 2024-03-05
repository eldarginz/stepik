n = int(input())
words = []

for i in range (0,n):
    text_buffer = input()
    if text_buffer not in words:
        words.append(text_buffer)

print(*words, sep='\n')