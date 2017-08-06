[x,y]=prompt().split(" ").map(x=>x-0)
!x?!y?'Origem':'Eixo X':!y?'Eixo Y':x>0?y>0?"Q1":"Q4":y>0?"Q2":"Q3"