for B in range(1, 11):
    for K in range(1, 21):
        for T in range(1, 200):
            if B*10 + K*5 + T*0.5 == 100:
                if B + K + T == 100:
                    print(B, K, T)



