def z(p)print "Data #{p}: ";gets.split(/\//).map(&:to_i)end
a,b,c=z"Atual"
d,e,f=z"de Nascimento"
i=d-a
h=e-b-(i<0?1:0)
h=(h<0?12+h:h)*30+(i<0?30+i:i)
puts"Idade: #{c-f-((e>b||e==b&&d>a)?1:0)}","Faltam #{h} dias, #{["Parabens","Aguarde"][h>0?1:0]}!"
