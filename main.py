from datetime import date
import os

# capturando data
anoatual = date.today()


## Calculando ano e Pergutando em que ano o usuario nasceu
def main():
	
	ano_informado = int(input("Informe o  ano voce nasceu? "))

	# Subtrair o ano atual do ano informado
	idade_ano = anoatual.year - ano_informado

	##### Calculando meses
	mes_informado = int(input("informe o  mes voce nasceu? "))

	# subtrai o mes atual do ano informado
	idade_mes = anoatual.month - mes_informado

	#Calculando dias
	dia_informado = int(input("Informe o dia voce nasceu? "))

	# subtrai o mes atual do ano informado
	idade_dia = anoatual.day - dia_informado

	# Realizando calculo final - mostrando idade correta
	

	if idade_mes < 0:
		idade_ano = idade_ano - 1

		idade_mes = abs(idade_mes)	


		# Imprimir na tela a idade calculada
	print("Voce tem", idade_ano, "ano(s) de idade", idade_mes, "mes(es) e" , idade_dia, "dia(s).")

# chamando funcao
main()
