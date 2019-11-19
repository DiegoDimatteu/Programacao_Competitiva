
import math
n, m, a = [int (i) for i in input().split()]
n = math.ceil(n / a)
m = math.ceil(m / a)
x = n * m
print(x)