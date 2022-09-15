wert = input()

a,b,c = wert.split()

m1 = int(b) - int(a)
m2 = int(c) - int(b)

if (m2 > m1):
    print(":)")
elif (m2 < m1):
    print(":(")
else:
    if (m1 <= 0):
        print(":(")
    else:
        print(":)")
