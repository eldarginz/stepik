text = input()

if text.count('f') == 0:
    print('NO')
else:
    if text.count('f') > 1:
        print(text.find('f'), text.rfind('f'))
    else:
        print(text.find('f'))