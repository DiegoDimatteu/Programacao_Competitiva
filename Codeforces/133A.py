a = input()
for i in range(len(a)):
	if a[i] == 'H' or a[i] == 'Q' or a[i] == '9':
		print('YES')
		exit()
print('NO')