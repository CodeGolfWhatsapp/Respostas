v=(0,6,13,-5)
a,b,c=map(int,input().split())
p=(a<3)*v[a]+v[b]
t=p+v[c]
print((p>24or t>24)*('Paz Mundial!\nQuantidade de tijolos: '+str([t,p][t<25]))or'Guerraaaa!')