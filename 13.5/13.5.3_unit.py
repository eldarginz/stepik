# объявление функции
def is_prime(num):
    if num == 1:
        return False
    d = 2
    while n % d != 0:
        d += 1
    return d == n


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
