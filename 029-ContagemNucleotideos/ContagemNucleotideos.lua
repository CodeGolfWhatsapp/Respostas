x=io.read()
a=0
t=0
c=0
g=0
for i in string.gmatch(x,".") do
if i=="A" then a=a+1
elseif i=="T" then t=t+1
elseif i=="C" then c=c+1
elseif i=="G" then g=g+1
end
end
io.write(a," ",c," ",g," ",t)