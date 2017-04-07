def raw_input():
	return 'CARLOS COSTA'

m=' ETIANMSURWDKGOHVF_L_PJBXCYZQ__54_3___2__+____16=/_____7___8_90'
o=''
for x in raw_input():
	c=m.index(x)
	if x==' ':
		o+='/'	
	while c>0:
		o+='-.'[c%2]
		c=(c-1)/2
	o+=' '
print o
