M,N=gets.split.sort
B=*M.to_i..N.to_i
puts B*" ","Soma=%d"%B.inject(:+)
