'''
Link da questão: https://codeforces.com/problemset/problem/112/A
'''
a = input()
b = input()
 
a = a.lower()
b = b.lower()
 
if a > b:
	print('1')
elif b > a:
	print('-1')
else:
	print('0')
