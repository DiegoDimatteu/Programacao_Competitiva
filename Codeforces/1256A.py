rep = int(input())
for j in range (rep):
	a, b, n, s = [int(i) for i in input().split()]
	if n <= s:
		aux = int(s/n)
		if aux > a:
			s -= n * a
			saida_a = 1
		else:
			s -= n * aux
			saida_a = 1
 
	if 1 <= s:
			aux = int(s/1)
			if aux > b:
				s -= 1
				saida_b = 1
			else:
				s -= aux
				saida_b = 1
	if s == 0:
		print('YES')
	else:
		print('NO')