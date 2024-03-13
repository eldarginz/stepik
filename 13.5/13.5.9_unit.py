# объявление функции
def is_correct_bracket(text):
    counter = 0
    for i in text:
        if i == '(':
            counter += 1
            # print(counter)
        if i == ')':
            counter -= 1
            # print(counter)
        if counter < 0:
            return False
    if counter == 0:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
