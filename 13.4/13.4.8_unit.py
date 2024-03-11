# объявление функции
def get_factors(num):
    result = []
    for i in range(1, num+1):
        if (num % i == 0):
            result.append(i)
    return (result)


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
