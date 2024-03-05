text = input().lower().split()

print('Общее количество артиклей:', text.count(
    'a')+text.count('an')+text.count('the'))
