num = int(input())
while num > 9:
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum += last_digit
        num = num // 10
    else:
        num = sum
else:
    print(num)