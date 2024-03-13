# объявление функции
def is_prime(num):
    if num == 1:
        return False
    d = 2
    while num % d != 0:
        d += 1
    return d == num


def is_valid_password(password):
    counter = 0
    text = password.split(':')
    if len(text) != 3:
        return False

    test0 = text[0]
    test1 = int(text[1])
    test2 = int(text[2])

    if test0 == test0[::-1]:
        counter += 1
        # print('test0 pass')

    if is_prime(test1):
        counter += 1
        # print('test1 pass')

    if test2 % 2 == 0:
        counter += 1
        # print('test2 pass')

    if counter == 3:
        return True
    else:
        return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
