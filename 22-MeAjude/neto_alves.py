#python 3.6

def comparar(a, b):
    if a > b:
        mensagemMaior(1, a)
    elif a < b:
        mensagemMaior(2, b)
    else:
        mensagemIgual()
    

def mensagemMaior(string, valor):
    if string == 1:
      string = "Primeiro"
    else:
      string = "Segundo"
    print("%s\nMaior Area: %d" %(string,valor) )

def mensagemIgual():
    print("Empate")


def verificar(valor):
    if(valor >= 0 and valor <= 100):
        return True
    else:
        return False

def converter(entrada):
    saida = entrada.split(" ")
    return int(saida[0]), int(saida[1])


def ajudar(a, b, c, d):
    if verificar(a) and verificar(b) and verificar(c) and verificar(d):
        comparar(a*b, c*d)
    else:
        print("Valor invalido")


e = input()
s = input()
a, b = converter(e)
c, d = converter(s)
ajudar(a, b, c, d)
