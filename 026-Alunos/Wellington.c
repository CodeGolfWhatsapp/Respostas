#include<stdio.h>
int main(){char n[50];float p[3],s=0;int i=0;fgets(n,50,stdin);for(;i<2;i++){scanf("%f",&p[i]);s+=p[i];}p[i]=s/2;printf("NOME: %s",n);for(i=0;i<2;i++){printf("NOTA %d: %.1f\n",i+1,p[i]);}printf("MEDIA: %.1f\n",p[i]);puts(p[i]>7?"APROVADO":"REPROVADO");}
