#A. Hulk
 
n = int(input())
i = 1
while i < n or i == n:
	if i == n:	
		if i % 2 == 0:
			print("I love it", end = '')
		else:
			print("I hate it", end = '')
	else:
		if i % 2 == 0:
			print("I love that ", end = '')
		else:
			print("I hate that ", end = '')
	i = i + 1
print()