a = input()
count_0 = 0
count_1 = 0
 
for i in range (len(a)):
	if a[i] == '0':
		count_0 += 1
		count_1 = 0
		if count_0 >= 7:
			print('YES')
			exit()
	else:
		count_1 += 1
		count_0 = 0
		if count_1 >= 7:
			print('YES')
			exit()
 
print('NO')