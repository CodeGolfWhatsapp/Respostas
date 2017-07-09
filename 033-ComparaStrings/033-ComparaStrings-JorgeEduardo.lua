a,b=io.read(),io.read()
print(a:len()==b:len() and "True" or "False")
if a:sub(1,1)==b:sub(1,1) and a:sub(-1)==b:sub(-1) then
print("True")
else
print("False")
end