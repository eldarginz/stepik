# x = a^3 + b^3 = c^3 d^3
  

for i in range(1, 1000):
    for j in range(1, 1000):
        for n in range(1, 1000):
            for y in range(1, 1000):
                if i != j and i != n and i != y and j != n and j != y and n!= y:
                       if (i**3 + j**3) == (n**3 + y**3):
                              print(i**3 + j**3)
                              print('a =', i, 'b =', j, 'c =', n, 'd =', y)