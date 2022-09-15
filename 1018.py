troco = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]

if troco > 0:
	print(troco)
	for p in notas:
		if troco >= p:
			n = int(troco/p)
			r = troco - p*n
			print ('%s nota(s) de R$ %s,00' % (n, p))
			troco = r
		else:
			print ('0 nota(s) de R$ %s,00' %p)
