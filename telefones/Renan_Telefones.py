t="";n="22233344455566677778889999"
for c in input():
	for i in range(26):
		if c==chr(65+i):t+=n[i];break
	else:t+=c
print(t)