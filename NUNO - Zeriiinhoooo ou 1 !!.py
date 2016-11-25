p='ABC';v=input()
for c in v:
	if v.count(c)==3:print('*');break
	if v.count(c)==1:print(p[v.index(c)])