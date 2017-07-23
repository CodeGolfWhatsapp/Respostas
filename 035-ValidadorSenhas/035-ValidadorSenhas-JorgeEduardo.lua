s=io.read()
if string.len(s)<6 or string.len(s)>32 then
print("SENHA INVALIDA")
elseif(s:match("%W")) then
print("SENHA INVALIDA")
else
print("SENHA VALIDA")
end
