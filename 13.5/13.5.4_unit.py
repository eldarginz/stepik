# объявление функции
def is_prime(num):
    if num == 1:
        return False
    d = 2
    while num % d != 0:
        d += 1
    return d == num


def get_next_prime(num):
    num += 1
    while is_prime(num) == False:
        num += 1
    return (num)


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
