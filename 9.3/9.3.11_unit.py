text = input()
counter = 0

for i in range (0, len(text)):
      if text[i] == text.lower()[i] and text[i] not in '0123456789':
          counter += 1
print(counter)