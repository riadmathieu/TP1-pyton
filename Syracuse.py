
def syracuse(p):
    s = []
    while p != 1:
        print(p,end = ',')
        if (p%2==1) :
            p = p*3+1
        else:
            p = p // 2
syracuse(6)