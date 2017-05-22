z=input();x=float(input());c=float(input());i=(x+c)/2;l=['NOME:','NOTA 1:','NOTA 2:','MEDIA:']
print(l[0],z);print(l[1],x);print(l[2],c);print(l[3],'%.1f'%i)
if i<=7:print('STATUS: REPROVADO')
else:print('STATUS: APROVADO')