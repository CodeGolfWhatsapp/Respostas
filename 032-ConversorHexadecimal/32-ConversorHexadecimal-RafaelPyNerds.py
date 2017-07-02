x=input();d=''
while x>0:d+='ABCDEF'[x%16-10] if x%16>9 else str(x%16);x/=16
print(d[::-1])
