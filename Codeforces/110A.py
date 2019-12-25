'''
Link da questão: https://codeforces.com/problemset/problem/110/A
'''
a = input()
cont = 0
count = 0
i = 0
while i < len(a):
	if a[i] == '7' or a[i] == '4':
		cont += 1
	i += 1
if cont == 4 or cont == 7:
	print('YES')
else:
	print('NO')
