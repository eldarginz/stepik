import random
def generate_password(lenght, chars):
    password = ''
    for i in range(lenght):
        password += random.choice(chars)
    return password

print(generate_password(8, '12owes9qwe802'))