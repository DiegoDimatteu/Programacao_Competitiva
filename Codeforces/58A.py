a = input()
i = 0
for j in range (len(a)):
	if i == 0:
		if a[j] == 'h':
			i = 1
	elif i == 1:
		if a[j] == 'e':
			i = 2
	elif i == 2:
		if a[j] == 'l':
			i = 3
	elif i == 3:
		if a[j] == 'l':
			i = 4
	elif i == 4:
		if a[j] == 'o':
			i = 100
if i == 100:
	print('YES')
else:
	print('NO')