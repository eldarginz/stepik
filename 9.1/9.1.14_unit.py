text = input()

vowel_letters = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
consonant_letters = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'

vowel_counter = 0
consonant_counter = 0

for i in range (0, len(text)):
    if text[i] in vowel_letters:
        vowel_counter += 1
    if text[i] in consonant_letters:
        consonant_counter += 1

print('Количество гласных букв равно', vowel_counter)
print('Количество согласных букв равно', consonant_counter)