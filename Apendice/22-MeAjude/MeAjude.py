i=raw_input
a,b,c,d=map(int,(i()+" "+i()).split())
s="o\nMaior area: "
e=a*b
f=c*d
print(("Segund"+s+`f`,"Primeir"+s+`e`)[e>f],"Empate")[e==f]
