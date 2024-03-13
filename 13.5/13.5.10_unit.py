# объявление функции
def convert_to_python_case(text):
    s = text[0]
    for i in range(1, len(text)):
        if text[i].isupper():
            s += '_' + text[i]
        else:
            s += text[i]
    return (s.lower())


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
