#include<stdio.h>
int main(){int a,t=0,i=0;for(;i<3;i++){scanf("%d",&a);t+=a==1?6:a==2?13:a==3&t>5&t<25?-5:0;}t>24?printf("Paz Mundial!\nQuantidade de tijolos: %d",t):puts("Guerraaaa!");}
