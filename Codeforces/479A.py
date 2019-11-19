a = int(input())
b = int(input())
c = int(input())
maior = 0
 
atual = a * b * c
if atual > maior:
	maior = atual
 
atual = (a + b) * c
if atual > maior:
	maior = atual
 
atual = a * (b + c)
if atual > maior:
	maior = atual
 
atual = a + b + c
if atual > maior:
	maior = atual
 
print(maior)