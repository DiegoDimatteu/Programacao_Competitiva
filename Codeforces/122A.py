a = int(input())
saida = 0
if(a % 4 == 0) or (a % 7 == 0):
		print('YES')
		saida = 1
elif a % 47 == 0:
	print('YES')
	saida = 1
while saida == 0:
	if  (a % 10 == 7) or (a % 10 == 4):
		a -= (a % 10)
	elif (a % 100 == 70) or (a % 100 == 40):
		a -= (a % 100)
	elif (a % 1000 == 700) or (a % 1000 == 400):
		a -= (a % 1000)
	elif a == 0:
		print('YES')
		saida = 1
	else:
		print('NO')
		saida = 1