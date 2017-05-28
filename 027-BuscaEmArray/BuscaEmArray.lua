math.randomseed(os.time())
t={}
for i=1,12 do
t[i]=math.random(0,99)
end
print(table.concat(t,","))
io.write("DIGITE UM NUMERO: ")
n=io.read("*n")
for k,v in ipairs(t) do
if v==n then
io.write("O NUMERO ",n," ESTA NA POSICAO ",k)
return
end
end
io.write("O NUMERO ",n," NAO SE ENCONTRA NO ARRAY.")