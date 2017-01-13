puts"IMC: #{i=(gets.to_i/gets.to_f**2).round 2}
Situacao: #{i<25?i<20?"Abaixo do Peso":"Peso Normal":i<34?i<30?"Acima do Peso":"Obeso":"Muito Obeso"}"
