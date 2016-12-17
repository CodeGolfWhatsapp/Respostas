T=int(input())
L=input().split(" ")[0:T]
E=int(L[0])
P=0
R=0
for(ele in L):
	P = R if( int(ele) < int(L[P]) ) else P
	R = R + 1
print("Menor valor: %s\nPosicao: %d" %(L[P],P))