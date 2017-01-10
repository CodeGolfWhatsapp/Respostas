i=input
m=int(i())/float(i()**2)
s,p,o="Situacao:","Peso","Obeso"
print "IMC:","%.2f"%m,"\n"+s,["","Abaixo do "+p][m<20]+["",p+" Normal"][20<m<25]+["","Acima do "+p][25<m<30]+["",o][30<m<34]+["","Muito "+o][34<m]
