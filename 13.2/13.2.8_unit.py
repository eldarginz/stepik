# объявление функции
def draw_triangle(fill, base):
    count = base // 2

    for i in range(count):
        for j in range(i + 1):
            print(fill, end='')
        print('')

    for j in range(count + 1):
        print(fill, end='')
    print('')

    for i in range(count, 0, -1):
        for j in range(i):
            print(fill, end='')
        print('')


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
