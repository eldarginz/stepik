# объявление функции
def is_one_away(word1, word2):
    counter = 0
    if word1 == word2:
        return False
    else:
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                counter += 1
                # print(counter)
    if counter+1 == len(word1):
        return True
    else:
        return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
