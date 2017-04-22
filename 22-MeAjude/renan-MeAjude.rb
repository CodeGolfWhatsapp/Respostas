d,e,f,g=(gets+gets).split.map &:to_i
s="o
Maior area: "
a=d*e
b=f*g
puts a==b ?"Empate":a>b ?"Primeir#{s}%d"%a:"Segund#{s}%d"%b
