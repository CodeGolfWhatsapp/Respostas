<?php $m="combustivel";echo"Informe a distancia em KM: ";$a=fgets(STDIN);echo"Informe o consumo medio: ";$c=$a/fgets(STDIN)+.5;echo sprintf("Total em Litros de $m: %u litros\nTotal gasto com $m: R$ %.2f\nParadas previstas: %u",$c,$c*3.8,$a/250);
