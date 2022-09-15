while True:
    qtd = int(input())
    if qtd ==0:
        break
    x = list(map(int,input().split()))
    c = 0
    j = 0
    for i in x:
        if i == 0:
            c += 1
        else:
            j += 1
    print("Mary won %d times and John won %d times" %(c,j))
