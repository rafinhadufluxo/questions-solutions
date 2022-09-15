wert = input()
A,B= wert.split()
a = int(A)
b = int(B)
if a%b == 0 or b%a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")