N = int(input())

count = 1
quantia = 0
coelho = 0
rato = 0
sapo = 0
cobaias = 0

while count <= N:
    quantia = input()
    valor,tipo = quantia.split()
    if tipo == 'C':
        coelho = coelho + int(valor)
    elif tipo == 'R':
        rato = rato + int(valor)
    elif tipo == 'S':
        sapo = sapo + int(valor)
    count += 1

cobaias = coelho+rato+sapo
perC = (coelho*100)/cobaias
perR = (rato*100)/cobaias
perS = (sapo*100)/cobaias

print("Total: {} cobaias". format (cobaias))
print("Total de coelhos: {}" . format(coelho))
print("Total de ratos: {}". format (rato))
print("Total de sapos: {}". format(sapo))
print("Percentual de coelhos: {:.2f} %". format(perC))
print("Percentual de ratos: {:.2f} %". format(perR))
print("Percentual de sapos: {:.2f} %" . format(perS))