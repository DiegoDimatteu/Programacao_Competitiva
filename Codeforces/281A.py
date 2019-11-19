a = input()
i = 0
while i < len(a):
	if i == 0:
		print(a[i].upper(), end = '')
	elif i == len(a) - 1:
		print(a[i])
	else:
		print(a[i], end = '')
	i += 1 