i=prompt().split(' ');m=[,6,13,-5];t=0;for(n in i){n=i[n];t+=((t+m[n])<0?0:m[n]);if(t>24)break};alert(t>24?'Paz Mundial!\nQuantidade de tijolos: '+t:'Guerraaaa!')
