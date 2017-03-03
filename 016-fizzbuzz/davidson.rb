puts (1..gets.to_i).map{|i|j=i%3>0?'':'fizz';j+=i%5>0?'':'buzz';j>''?j:i}*', '
