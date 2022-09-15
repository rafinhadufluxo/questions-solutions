while True:
    wert = input()
    M,N = wert.split()
    x = int(M)
    y = int(N)
    if x <= 0 or y <= 0:
        break
    else:
        folgenden = []
        snum = 0
        if x > y:
            for z in range(y,x+1):
                snum += z
                print(z,end=" ")

        else:
            for z in range(x,y+1):
                snum = snum + z
                print(z,end=" ")
        print("Sum=%d" %snum)