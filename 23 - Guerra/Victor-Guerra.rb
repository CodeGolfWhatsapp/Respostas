c=t=0
while(a=gets.to_i)
a<2?t+=6:
a>2?t-=5:t+=13
t=0 if t<0
break if t>24||c>1
c+=1
end
puts t>24 ?"Paz Mundial!\nQuantidade de tijolos:#{t}":"Guerraaaa!"
