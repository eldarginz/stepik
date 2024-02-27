a, b = int(input()), int(input())

mx_num = -1
mx_sum = -1
for cur_num in range(a, b + 1):
    cur_sum = 0
    for j in range(1, cur_num + 1):
        if cur_num % j == 0:
            cur_sum += j

    if cur_sum >= mx_sum:
        mx_num = cur_num
        mx_sum = cur_sum

print(mx_num, mx_sum)