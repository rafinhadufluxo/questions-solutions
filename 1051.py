rombus = float(input())

if rombus <= 2000.00:
    print("Isento")
elif rombus <= 3000.00:
    imposto = (rombus - 2000.00) * 0.08
    print("R$ %.2f" % imposto)
elif rombus <= 4500.00:
    faixa1 = 80.00
    imposto = ((rombus - 3000.00) * 0.18) + faixa1
    print("R$ %.2f" % imposto)
elif rombus > 4500.00:
    faixa2 = 350.00
    imposto = ((rombus - 4500.00) * 0.28) + faixa2
    print("R$ %.2f" % imposto)