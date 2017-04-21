def f():a,b=map(int,input().split());return a*b
a=f()
b=f()
print((a>b)*'Primeiro'+(a<b)*'Segundo'or'Empate',(a!=b)*('\nMaior area: '+str(max(a,b))))