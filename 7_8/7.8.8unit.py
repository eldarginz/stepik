n = int(input())
count = n//2



for i in range(count):
    for j in range(i+1):
        print('*', end='')
    print('')

for j in range(count+1):
    print('*', end='')
print('')

for i in range(-count, 1):
    for j in range(i+1):
        print('*', end='')
    print('')