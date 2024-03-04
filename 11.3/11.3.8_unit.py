output = []

for i in range(97, 123):
    output.extend(chr(i))
    output[-1] *= i-96
print(output)
