p=io.write
q="\nMaior Área "
a,b=io.read("*n","*n")
c,d=io.read("*n","*n")
e=a*b;f=c*d
if e>f then p("Primeiro",q,e)
elseif f>e then p("Segundo",q,f)
else p("Empate")
end
