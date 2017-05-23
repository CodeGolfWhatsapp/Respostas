a=Array.new
a[0]=gets
a[1]=gets
a[2]=gets
m=(a[1].to_f+a[2].to_f)/2
$t=m<=7
puts"NOME: "+a[0]
puts"NOTA 1: "+a[1]
puts"NOTA 2: "+a[2]
puts"MEDIA: "+m.to_s
print"STATUS: "
print"REPROVADO"if $t
print"APROVADO"unless $t