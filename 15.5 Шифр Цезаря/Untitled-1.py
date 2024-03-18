def cezar (isx,k):
    isx="Day"
    k=3
    abc = ('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z').split()
    #print(abc)
    str=''
    for i  in range(len(isx)):
        if isx[i].upper() not in (abc):
            str +=(isx[i])
        if isx[i].upper() in (abc):
            c = abc[(abc.index(isx[i].upper()) + k) % len(abc)]
            if isx[i].isupper():
                str +=c.upper()
            else:
                str += c.lower()
    return(str)

text = input()
print(text.split(' '))
