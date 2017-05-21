u="\nNota";l=input;z=[0]*4;z[0]=l();z[1]=float(l());z[2]=float(l());z[3]=(z[1]+z[2])/2
if z[3]<=7:print("Nome:",z[0],u,"1:",z[1],u,"2:",z[2],"\nMedia:",z[3],"\nStatus: REPROVADO")
else:print("Nome:",z[0],u,"1:",z[1],u,"2:",z[2],"\nMedia:",z[3],"\nStatus: APROVADO")