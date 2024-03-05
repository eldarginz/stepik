def palindrom(num):
    temp = num
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if (temp == rev):
        return True
    else:
        return False


palindromes = [i for i in range(100, 1001) if palindrom(i)]

print(palindromes)
