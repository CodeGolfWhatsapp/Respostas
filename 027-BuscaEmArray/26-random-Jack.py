from random import*
a,p=sample(range(99),12),print
p(str(a).lstrip("[").rstrip(']'));r=int(input("DIGITE UM NUMERO DE 0 A 99:\n"))
if r in a:p("O NUMERO",r,"ESTA NA POSICAO",a.index(r))
else:p("O NUMERO",r,"NAO ESTA NA ARRAY")