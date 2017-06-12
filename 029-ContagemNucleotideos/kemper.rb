h=Hash.new(0)
(gets.split '').each{|i|h[i]+=1}
print [h[?A],h[?C],h[?G],h[?T]]*' '
