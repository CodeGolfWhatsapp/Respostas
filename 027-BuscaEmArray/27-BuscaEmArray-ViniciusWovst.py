import random,re
n='O NUMERO';l=random.sample(range(100),12);p=print
p(re.sub('[[\]]','',str(l)));
v=int(input('DIGITE UM NUMERO DE 0 A 99:\n'))
if v in l:p(n,v,'ESTA NA POSICAO',l.index(v))
else:p(n,v,'NAO SE ENCONTRA NO ARRAY.')
