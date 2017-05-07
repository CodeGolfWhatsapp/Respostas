#python 3.6

def entrada(valor):
	valor = int(valor)
	if 1 <= valor and valor <= 100000:
		return valor
	return None

def soma(valorA, valorB):
	print("SOMA = %d" % (entrada(valorA) + entrada(valorB)))

def multiplicacao(valorA, valorB):
	print("MULTIPLICACAO = %d" % (entrada(valorA) * entrada(valorB)))


def subtracao(valorA, valorB):
	print("SUBTRACAO = %d" % (entrada(valorA) - entrada(valorB)))

def contas(valorA, valorB):
	valorA = entrada(valorA)
	valorB = entrada(valorB)
	if valorA != None and valorB != None:
		if valorA >= valorB:
			soma(valorA, valorB)
			multiplicacao(valorA, valorB)
			subtracao(valorA, valorB)

entradas = input()
entradas = entradas.split(" ")
valorA = entradas[0]
valorB = entradas[1]
contas(valorA, valorB)