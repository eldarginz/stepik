text = input()
counter = 0

for i in range (0, 10):
    counter += text.count(str(i))

print(counter)