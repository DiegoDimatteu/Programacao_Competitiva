import math
 
n = int(input())
value = []
qtd = 0
value = [int(i) for i in input().split()]
value.sort(reverse = True)
i = 0
count = 0
while i < n and count <= sum(value) / 2:
	count += value[i]
	qtd += 1
	i += 1		
print(qtd)
 