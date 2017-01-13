w=int(input())
h=float(input())
i=w/h**2
if i<20:print("IMC: %.2f \nSituação: Abaixo do Peso" % (i))
elif 20<=i<24.9:print("IMC:  %.2f \nSituação: Peso Normal" % (i))
elif 24.9<=i<30:print("IMC: %.2f \nSituação: Acima do peso" % (i))
elif 30<=i<34:print("IMC: %.2f \nSituação: Obeso"  % (i))
else:print("IMC: %.2f \nSituação: Muito Obeso" % (i))