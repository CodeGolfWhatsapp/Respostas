l=int(input())
a=[]
for i in range(0,l):
    n=eval(input())
    a.append(n)
m=min(a)
p=a.index(min(a))
print('Menor valor:%d'%(m))
print('Posicao:%d'%(p))