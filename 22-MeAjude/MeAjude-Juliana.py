a,b=map(int,input().split())
c,d=map(int,input().split())
a=a*b
c=c*d
if a>c:print("Primeiro\nMaior area:",a)
elif c>a:print("Segundo\nMaior area: ",c)
else:print("Empate")
