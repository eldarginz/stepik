inputcount = int(input())
counter = 0
for i in range(0, inputcount):
    text = input()
    if text.count('11') >= 3:
        counter += 1

print(counter)