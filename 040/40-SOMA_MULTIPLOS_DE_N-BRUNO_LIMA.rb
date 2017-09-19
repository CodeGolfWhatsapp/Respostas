n=gets.to_i;s=0;(1..n).each{|i|s=(n%i==0)?s+i:s+0}
p s