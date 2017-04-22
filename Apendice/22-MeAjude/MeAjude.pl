@d=split/ /,<>." ".<>;
$s="o\nMaior area: ";
$a=@d[0]*@d[1];
$b=@d[2]*@d[3];
if($a==$b){print"Empate";}else{print$a>$b?"Primeir".$s.$a:"Segund".$s.$b}
