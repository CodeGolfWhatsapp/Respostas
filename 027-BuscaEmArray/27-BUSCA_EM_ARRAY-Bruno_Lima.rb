v=Array.new(12){rand 100}
puts v.join(', ')
b=gets.to_i
if v.include?b
puts"O NUMERO #{b} ESTA NA POSICAO #{v.index(b)}"
else puts"O NUMERO NAO SE ENCONTRA NO ARRAY"end