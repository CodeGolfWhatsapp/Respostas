C=gets.to_i/gets.to_r**2
puts"IMC: %.2f
Situacao: #{C<20?"Abaixo do peso":C<25?"Peso Normal":C<30?"Acima do peso":C<34?"Obeso":"Muito Obeso"}"%C
