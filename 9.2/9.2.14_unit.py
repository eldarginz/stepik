text = input()

if len(text) % 2 == 0:
    print(text[int(len(text)/2):]+text[:int(len(text)/2)])
if len(text) % 2 == 1:
    print(text[int(len(text)/2)+1:]+text[:int((len(text)/2)+1)])