w=io.write
r=io.read
s=string.format
t={}
t.X=r()
t.Y=r("*n")
t.Z=r("*n")
t.K=(t.Y+t.Z)/2
w("NOME: ",t.X,"\nNOTA 1: ",s("%.1f",t.Y),"\nNOTA 2: ",s("%.1f",t.Z),"\n",s("MEDIA: %.1f",t.K))
w(t.K>7 and "\nSTATUS: APROVADO" or "\nSTATUS: REPROVADO")