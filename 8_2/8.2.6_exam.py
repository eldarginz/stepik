def count3(x):
    # количество цифр 3 в нем
    counter = 0
    while x != 0:
        if x % 10 == 3:
            counter += 1
        x //= 10
    return counter
    
def lastnum(x):
    # сколько раз в нем встречается последняя цифра
    counter = 0
    last = x % 10
    while x != 0:
        if x % 10 == last:
            counter += 1
        x //= 10
    return counter

def countchet(x):
    # количество четных цифр
    counter = 0
    while x != 0:
        if (x % 10) % 2 == 0:
            counter += 1
        x //= 10
    return counter

def sumbolsh5(x):
    # сумму его цифр, больших пяти
    max = 0
    while x != 0:
        if x % 10 > 5:
            max += x % 10
        x //= 10
    return max

def proizbolsh7(x):
    # произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее)
    counter = 0
    max = 1
    while x != 0:
        if x % 10 > 7:
            max *= x % 10
            counter += 1
        x //= 10
    if counter == 0:
        max = 1
    return max

def skolko05(x):
    # сколько раз в нем встречаются цифры 0 и 5 (всего суммарно)
    counter = 0
    while x != 0:
        if x % 10 == 0 or x % 10 == 5:
            counter += 1
        x //= 10
    return counter

num = int(input())

print(count3(num))
print(lastnum(num))
print(countchet(num))
print(sumbolsh5(num))
print(proizbolsh7(num))
print(skolko05(num))
