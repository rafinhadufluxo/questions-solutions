numberOfValues = int(input())

expenses = 0
funds = 0

for currentValue in range(numberOfValues):
    valueInput = input().split(' ')

    transaction = str(valueInput[0])
    value = int(valueInput[1])

    if(transaction == 'G'):
        expenses += value
    elif (transaction == 'V'):
        funds += value

if(funds >= expenses):
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')