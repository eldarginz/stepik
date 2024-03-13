# объявление функции
def is_palindrome(text):
    text1 = ''.join(i for i in text.lower() if i.isalpha())
    if text1 == text1[::-1]:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
