#text = input()
#
#for i in range (1, len(text)):
#    if i%3 != 0:
#        print(text[i], end='')

#text = input()
#
#if text.count('f') == 0:
#    print('-2')
#elif text.count('f') == 1:
#    print('-1')
#elif text.count('f') > 1:
#    print(text.find('f', text.find('f')+1))

text = input()
start = text.find('h')
end = text.rfind('h')

for i in range(0,start+1):
    print(text[i], end='')
for i in range(end-1, start, -1):
    print(text[i], end='')
for i in range(end, len(text)):
    print(text[i], end='')