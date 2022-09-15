salario = float(input())

if salario <= 400.00:
	porcentagem = salario * (15/100)
	salario = salario + porcentagem
	print("Novo salario: {:.2f}". format(salario))
	print("Reajuste ganho: {:.2f}". format (porcentagem))
	print("Em percentual: 15 %")
	
	

elif salario <= 800.00:
	porcentagem = salario * (12/100)
	salario = salario + porcentagem
	print("Novo salario: {:.2f}". format(salario))
	print("Reajuste ganho: {:.2f}". format (porcentagem))
	print("Em percentual: 12 %")


elif salario <= 1200.00:
	porcentagem = salario * (10/100)
	salario = salario + porcentagem
	print("Novo salario: {:.2f}". format(salario))
	print("Reajuste ganho: {:.2f}". format (porcentagem))
	print("Em percentual: 10 %")

elif salario <= 2000.00:
	porcentagem = salario * (7/100)
	salario = salario + porcentagem
	print("Novo salario: {:.2f}". format(salario))
	print("Reajuste ganho: {:.2f}". format (porcentagem))
	print("Em percentual: 7 %")

else:
	porcentagem = salario * (4/100)
	salario = salario + porcentagem
	print("Novo salario: {:.2f}". format(salario))
	print("Reajuste ganho: {:.2f}". format (porcentagem))
	print("Em percentual: 4 %")