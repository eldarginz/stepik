numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

maxpos = numbers.index(max(numbers))
minpos = numbers.index(min(numbers))
maxbuffer = max(numbers)
minbuffer = min(numbers)

numbers[maxpos] = minbuffer
numbers[minpos] = maxbuffer

print(*numbers)
