wert = input()
A,B = wert.split()
a = int(A)
b = int(B)
if (a < 0) and (b < 0):
    abteilung = divmod(abs(a), b)# divmod faz a divisão dos numeros
    print("%d %d" % (abs(abteilung[0]), abs(abteilung[1]))) #abs retorna o valor + ou -

elif (a < 0):
     abteilung = divmod(abs(a), -(b))
     print("%d %d" %(abteilung[0], abs(abteilung[1])))

elif (b < 0):
     abteilung = divmod(-(a), b)
     print("%d %d" %(abteilung[0] * (-1), abs(abteilung[1])))

else:
     abteilung = divmod(a, b)
     print("%d %d" %(abteilung[0], abs(abteilung[1])))