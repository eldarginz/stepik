# Программа генерирует число от 1 до 100, игроку надо угадать его
# Если число игрока больше загаданного, нужно вывести сообщение, что число большое
# Если число игрока меньше загаданного, нужно вывести сообщение, что число меньше
# Если число равно загаданному, нужно вывести сообщение, что число угадано

import random
num = random.randint(1,100)

def is_valid(num):
    if int(num) < 0 or int(num) > 100:
        return False
    else:
        return True

#print(num)
counter = 1

print ('Попробуй угадать загаданное число:')
while True:
    user_num = int(input('Введите число от 1 до 100: '))
    
    if is_valid(user_num):
        if user_num > num:
            print('Число слишком большое, попробуй еще раз')
            counter += 1
        elif user_num < num:
            print('Число слишком маленькое, попробуй еще раз')
            counter += 1
        else:
            print('Число угадано за ', counter, ' попыток')
            break
    else:
        print('ты че?')