'''
Link da questão: https://codeforces.com/problemset/problem/148/A
'''
k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
count = 0
 
if k > d and l > d and m > d and n and d:
	print(count)
	exit()
 
for i in range (1, d + 1):
	if i % k == 0:
		pass
	elif i % l == 0:
		pass
	elif i % m == 0:
		pass
	elif i % n == 0:
		pass
	else:
		count += 1
 
print(d - count)
