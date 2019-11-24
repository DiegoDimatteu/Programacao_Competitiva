'''
Link da questão: https://codeforces.com/problemset/problem/41/A
'''

a = list(input())
b = list(input())
a.reverse()
if a == b:
	print('YES')
else:
	print('NO')
