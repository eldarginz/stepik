# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0].upper(), end='')
    print(name[0].upper(), end='')
    print(patronymic[0].upper(), end='')


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
