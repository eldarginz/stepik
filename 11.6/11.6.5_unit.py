numbers = [8, 9, 10, 11]
del numbers[1]
numbers.insert(1, 17)

for i in range(3):
    numbers.append(i+4)

del numbers[0]

for i in range(len(numbers)):
    numbers.append(numbers[i])

numbers.insert(3, 25)

print(numbers)

'''
numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)
'''