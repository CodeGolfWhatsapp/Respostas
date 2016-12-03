a=input();t='';q='ABCDEFGHIJKLMNOPQRSTUVWXYZ-0122233344455566677778889999-01'
for i in a:
	for j in range(29):
		if(i in q[j]):t=t+q[j+29]
print(t)