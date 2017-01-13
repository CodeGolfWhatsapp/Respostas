puts"IMC: %.2f"%m=gets.to_i/(gets.to_f**2).round(2),"Situacao: "+(m<20?"Abaixo do Peso":m<25?"Peso Normal":m<30?"Acima do Peso":m<34?"Obeso":"Muito Obeso")
