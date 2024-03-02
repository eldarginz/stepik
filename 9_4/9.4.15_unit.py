text = input()

start = text.find('h')
end = text.rfind('h')

print(text[:start],text[end+1:], sep='')