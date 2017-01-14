i=input()/input()**2
if i<20:s='abaixo do peso'
elif i<24:s='peso normal'
elif i<30:s='acima do peso'
elif i<34:s='obeso'
else:s='muito obeso'
print'%.2f'%i,'\nSituacao: %s'%s
