# объявление функции
def is_password_good(password):
    counter = 0
    if len(password) > 7:
        counter += 1
        # print('len')

    for i in range(len(password)):
        if password[i].islower():
            # print('lower')
            counter += 1
            break

    for i in range(len(password)):
        if password[i].isupper():
            # print('upper')
            counter += 1
            break

    for i in range(len(password)):
        if password[i].isdigit():
            # print('digit')
            counter += 1
            break

    if counter == 4:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
