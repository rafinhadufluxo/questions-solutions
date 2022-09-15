import os
os.system('clear')

from math import sqrt
def F(n):
	return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

num = int(input())

for x in range(0,num):
    
    if x < (num-1):
        
        print(F(x),end=" ")
    else:
        print(F(x))