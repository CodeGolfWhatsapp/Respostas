c=input();d=list(c)
for i in range(len(d)):
	if d[i]=="A":d[i]="T"
	elif d[i]=="T":d[i]="A"
	elif d[i]=="C":d[i]="G"
	elif d[i]=="G":d[i]="C"
print("A CADEIA DE DNA DIGITADA E:\n",c,"\nSUA CADEIA COMPLEMENTAR E:\n","".join(d),"\nA CADEIA COMPLETA E:\n",c,"\n","".join(d))
