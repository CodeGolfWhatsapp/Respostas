import random
n=random.sample(range(0,100),12)
print(",".join(map(str,n)))
x=int(input("DIGITE UM NUMERO DE 0 A 99:\n"))
for i in range(12):
	if x==n[i]:print("O NUMERO %d ESTA NA POSICAO %d"%(x,i));break
else:print("O NUMERO %d NAO SE ENCONTRA NO ARRAY"%(x))
