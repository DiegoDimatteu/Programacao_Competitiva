'''
Link da questão: https://codeforces.com/problemset/problem/116/A
'''
a = int(input())
i = 0
b, c = [int (i) for i in input().split()]
maior = c - b
soma = maior
while i < a - 1:
	b, c = [int (i) for i in input().split()]
	soma += c - b
	if soma > maior:
		maior = soma
	i += 1
print(maior) 
