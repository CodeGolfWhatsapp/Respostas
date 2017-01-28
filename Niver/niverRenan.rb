print"Data atual: ";d,m,a=gets.split("/").map &:to_i
print"Data de nascimento: ";e,n,b=gets.split("/").map &:to_i
i=a-b-(m>=n&&d>=e ?0:1)
s=30*(n-m)+e-d+(n<m||n==m&&e<d ?360:0)
puts"Idade: #{i} Anos
Faltam #{s} dias, #{s==0?"Parabens!":"espere!"}"
