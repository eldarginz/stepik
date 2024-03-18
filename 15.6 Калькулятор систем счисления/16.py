def hex_to_ten(num):
    num = list(num)
    num = ','.join(num)
    hex_ten_1 = ['10', '11', '12', '13', '14', '15']
    hex_ten_2 = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(6):
        num = num.replace(hex_ten_2[i], hex_ten_1[i])
    num = num.split(',')
    i = 0
    new_num = 0
    while num != []:
        new_num += int(num[-1]) * 16 ** i
        i += 1
        num = num[:-1]
    return new_num

print(hex_to_ten(input()))