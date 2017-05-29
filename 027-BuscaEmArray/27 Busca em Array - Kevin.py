import random
l=[]
for i in range(12):l.append(random.randint(0,99))
print str(l).strip('[').rstrip(']')
a=input("Digite um numero de 0 a 99: ")
print"O numero %d esta na posicao %d"%(a,l.index(a))if a in l else "Numero %d não encontrado no Array"%a