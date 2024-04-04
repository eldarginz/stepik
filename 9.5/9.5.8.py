word = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
rez = {True: 'YES', False: 'NO'}
t = input()

len_test = False
word_test = False
digit_test = False
mark_test = False

if len(t) == 9 or len(t) == 10:
    len_test = True

if t[0] in word and t[4:5] in word:
    word_test = True

if len(t) == 9:
    if t[1:3].isdigit() and t[-1:-2:-1].isdigit():
        digit_test = True

if len(t) == 10:
    if t[1:3].isdigit() and t[-1:-3:-1].isdigit():
        digit_test = True

if t[6] == '_':
    mark_test = True

test = len_test * word_test * digit_test * mark_test

print(rez[test])
