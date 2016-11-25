#include <stdio.h>
void main(){int a,b,c;scanf("%d%d%d",&a,&b,&c);if(a==b&&b==c)printf("*");else{if(a==b)printf("C");if(a==c)printf("B");if(b==c)printf("A");}}
