'''
Link da questão: https://codeforces.com/problemset/problem/1/A
'''

import math
n, m, a = [int (i) for i in input().split()]
n = math.ceil(n / a)
m = math.ceil(m / a)
x = n * m
print(x)
