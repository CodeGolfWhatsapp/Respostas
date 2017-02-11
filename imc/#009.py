i=int(input())
o=float(input())
a=i/o**2
print("IMC:%.2f. Abaixo do Peso"%a if a<20)
print("IMC:%.2f. Peso Normal"%a if 20<=a<25)
print("IMC:%.2f. Acima do peso"%a if 25<=a<30)
print("IMC:%.2f. Obeso"%a if 30<=a<34 else "IMC:%.2f. Muito Obeso"%a)