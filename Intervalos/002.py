a='Intervalo '
x=input()
print'Fora de '+a if x<0 or x>100 else a+('[0,25]'if x<=25 else'(25,50]'if x<=50 else'(50,75]'if x<=75 else'(75,100]')