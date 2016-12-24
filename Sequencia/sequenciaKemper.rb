i,j=gets.split.map(&:to_i).sort;puts [*i..j]*' ',"Total=#{(i+j)*(j-i+1)/2}"
