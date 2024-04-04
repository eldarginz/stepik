n = int(input())
deletemark = 'COMMENT SHOULD BE DELETED'

for i in range(n):
    a = input()
    if a.isspace() or len(a) < 1:
        a = deletemark
    print(f'{i+1}: {a}')
