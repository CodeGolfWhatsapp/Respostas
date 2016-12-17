a=[];c=0
for i in range(input()):
	a.append(input())
	if a[c]>a[i]:c=i
print'Menor valor:',+a[c]
print'Posicao:',+c