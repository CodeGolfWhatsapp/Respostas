x,i,y,j=gets.split.map(&:to_i)
x*=i
y*=j
t="o\nMaior Area:"
puts x>y ?"Primeir#{t}#{x}":
x<y ?"Segund#{t}#{y}":"Empate"