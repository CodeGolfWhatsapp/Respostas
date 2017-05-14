#include<stdio.h>
int main(){int a,b,i=0,j=0;scanf("%d%d",&a,&b);int c=a;for(;i<b;i++){i==0?puts("1"):i==1?printf("%i\n",a):0;for(;j<i-1;j++){printf("%i\n",c*=a);}}}
