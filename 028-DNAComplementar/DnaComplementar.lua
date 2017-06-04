x=io.read()
y=""
for i in string.gmatch(x,".") do
if i=="A" then y=y.."T"
elseif i=="T" then y=y.."A"
elseif i=="C" then y=y.."G"
elseif i=="G" then y=y.."C"
end
end
io.write("A CADEIA DE DNA DIGITADA E:\n",x,"\nSUA CADEIA COMPLEMENTAR E:\n",y,"\nA CADEIA COMPLETA E:\n",x,"\n",y)