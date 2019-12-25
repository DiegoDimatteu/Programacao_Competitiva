'''
Link da questão: https://codeforces.com/problemset/problem/131/A
'''
a = input()
if len(a) == 1 and a.islower():
	print(a.upper())
	exit()
if a.isupper():
	print(a.lower())
	exit()
if a[1:].isupper():
	print(a[0].upper(), end = '')
	print(a[1:].lower())
	exit()
else:
	print(a)
