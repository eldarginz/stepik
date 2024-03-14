# объявление функции
def is_magic(date):
    l = date.split('.')
    if (int(l[0]) * int(l[1]) == int(l[2][2:])):
        return True
    else:
        return False


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
