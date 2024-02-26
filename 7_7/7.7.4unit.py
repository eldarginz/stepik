# mx = 0
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s = x
#     if x > mx:
#         mx = x
# print(s)
# print(mx)

max = 0
sum = 0

for i in range(10):
    x = int(input())
    if x < 0:
        sum = sum + x
        if x > max:
            max = x
        else:
            print ("NO")
if sum==max:
    print ("NO")
else:
    print (sum)
    print (max)