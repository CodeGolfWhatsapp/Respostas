#python 3.6

def numero(valor):
	valor = int(valor)
	if 0 <= valor and valor <= 3:
		return valor
	return None

def calcula(somador, entrada):
	if entrada == 1:
		somador = somador + 6
	elif entrada == 2:
		 somador = somador + 13
	elif entrada == 3 and somador >= 5:
		 somador = somador - 5
	return somador 

def mensagem(soma):
	msg = ""
	if soma >= 25:
		msg = "Paz mundial!\n"
		msg += "Quantidde de Tijolos: "
		msg += str (soma)
	else:
		msg = "Gueraaaa!"
	print(msg)


entrada = input()
entrada = entrada.split (" ")

diaA = numero(entrada[0])
diaB = numero(entrada[1])
diaC = numero(entrada[2])

somador = 0
somador = calcula(somador, diaA)
somador = calcula(somador, diaB)
somador = calcula(somador, diaC)

mensagem(somador)
