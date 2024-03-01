text = input()

cache1 = 0
cache2 = 0

for i in text:
    if cache1 <= text.count(i):
        cache1 = text.count(i)
        cache2 = i

print(cache2)