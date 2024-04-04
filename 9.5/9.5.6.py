n = input()
answers = {True: 'Correct', False: 'Incorrect'}

at_check = False
len_check = False
lower_check = False
alnum_check = False

if n[0] == '@':
    at_check = True
if 5 <= len(n) <= 15:
    len_check = True
if n.islower() or n[1:].isdigit():
    lower_check = True
if n[1:].isalnum():
    alnum_check = True

print(answers[at_check*len_check*lower_check*alnum_check])
