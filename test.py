# Дано натуральное число. Напишите программу, которая вычисляет:
# 
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

#x = int(input())
#xlast = x % 10
#xfirst = int(0)
#xcounter = int(0)
#xsumma = int(0)
#xproiz = int(1)
#
#while x != 0:
#    xcounter += 1
#    xsumma += x % 10
#    xproiz *= x % 10
#    if x > 0:
#        xfirst = x
#    x //= 10
#
#print(xsumma)
#print(xcounter)
#print(xproiz)
#print(xsumma / xcounter)
#print(xfirst)
#print(xfirst + xlast)


print(5 // 10)
print('test')

def sumbolsh5(x):
    # сумму его цифр, больших пяти
    max = 0
    while x != 0:
        if x % 10 > 5:
            max += x
        x //= 10
    return max

print(sumbolsh5(56639))