a=list(map(int,input().split()))
s,c=0,""
for i in range(min(a),max(a)+1):
	s,c=s+i,c+"%i "%i
print("%s\nSoma=%s"%(c,s))