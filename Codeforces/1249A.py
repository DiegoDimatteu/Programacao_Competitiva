'''
Link da questão: https://codeforces.com/problemset/problem/1249/A
'''
a = int(input())
count = 1
for i in range (a):
	condicion = 0
	b = int(input())
	c = [int(i) for i in input().split()]
	c.sort()
	j = 1
	while j <= (len(c) - 1):
		if(c[j] - c[j - 1]) == 1:
			count = 2
			j = len(c)
		else:
			j += 1
	print(count)
	count = 1
 
 
