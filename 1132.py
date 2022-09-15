x = int(input())
y = int(input())

soma= 0

if x > y:
	for c in range (y,x +1):
		if c % 13 != 0:

			soma += c
else:
	for c in range(x, y+1):
		if c % 13 != 0:
			soma += c
			
print(soma)