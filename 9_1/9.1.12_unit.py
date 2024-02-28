text = input()
counter_plus = 0
counter_asterisk = 0

for i in range (0, len(text)):
    if text[i] == '+':
        counter_plus += 1
    if text[i] == '*':
        counter_asterisk += 1

print('Символ + встречается', counter_plus, 'раз')
print('Символ * встречается', counter_asterisk, 'раз')