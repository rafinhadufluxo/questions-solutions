par = impar = 0
for c in range(5):
    x = int(input())
    if x % 2 == 0:
        par += 1
    else:
        impar += 1

print("{} valores pares". format(par))