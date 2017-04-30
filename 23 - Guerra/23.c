#include<stdio.h>
main(){
    int A,b=0,c=0;
    while(scanf("%d",&A)!=EOF){c++;
    if(A==1)b+=6;
    if(A==2)b+=13;
    if(A==3)if(b>=5)b-=5;
    if(c==3||b>=25){ if(b<25)
        puts("Guerraaaaa!");
    else printf("Paz Mundial!\nQuantidade de tijolos: %d\n", b);
    b=0;c=0;fflush(stdin);}
    }
    return 0;
}
