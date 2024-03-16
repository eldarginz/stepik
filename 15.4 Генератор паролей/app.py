import random

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
NOSYMBOL = 'il1Lo0O'

chars = ''

def generate_password(lenght, chars):
    password = ''
    for i in range(lenght):
        password += random.choice(chars)
    return password

count_passwords = input('Количество паролей для генерации: ')
len_password = int(input('Длина пароля: '))
digits_flag = input('Включать ли цифры? (y/n) ')
uppercase_flag = input('Включать ли прописные буквы? (y/n) ')
lowercase_flag = input('Включать ли строчные буквы? (y/n) ')
punctuation_flag = input('Включать ли символы? (y/n) ')
nosymbol_flag = input('Исключать ли неоднозначные символы? (y/n) ')

if digits_flag.lower() == 'y':
    chars += DIGITS
if uppercase_flag.lower() == 'y':
    chars += UPPERCASE_LETTERS
if lowercase_flag.lower() == 'y':
    chars += LOWERCASE_LETTERS
if punctuation_flag.lower() == 'y':
    chars += PUNCTUATION
if nosymbol_flag.lower() == 'y':
    for c in NOSYMBOL:
        chars = chars.replace(c,'')

for j in range(int(count_passwords)):
    print(generate_password(len_password, chars))