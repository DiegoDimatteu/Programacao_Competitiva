a = int(input())
lista = [int(i) for i in input().split()]
count = 0
countM = 0
condicion = 0
i = 0
while i < a:
	if count == 0:
		if i != 0:
			i -= 1
		count += 1 	
	else:
		ant = lista[i - 1]
		atual = lista[i]
		if ant <= atual:
			count += 1
		else:
			if count > countM:
				countM = count
				count = 0
				condicion = 1
			else:
				count = 0
	i += 1
if count > countM:
	countM = count
if condicion == 0:
	countM = count
print(countM)
 