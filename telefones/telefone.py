s=raw_input()
t=''
for c in s:
	if c in'ABC':t=t+'2'
	if c in'DEF':t=t+'3'
	if c in'GHI':t=t+'4'
	if c in'JKL':t=t+'5'
	if c in'MNO':t=t+'6'
	if c in'PQRS':t=t+'7'
	if c in'TUV':t=t+'8'
	if c in'WXYZ':t=t+'9'
	if c=='1':t=t+'1'
	if c=='-':t=t+'-'
print(t)