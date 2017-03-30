j=0
l=gets
m=gets.split()
for i in m
j+=i.to_i%2==0?1:-1end
puts j==0?"S":"N"
