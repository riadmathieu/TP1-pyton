def multiplicationEgyptienne(i, p):
    proegypt = 0
    while i != 0:

        if i % 2 == 1:  
            proegypt += p
        i //= 2 
        p += p 
    print(proegypt)
    return proegypt
 
multiplicationEgyptienne(int(input()), int(input()))
 