p=int(input());a=float(input());i=p/a**2
if i<20:
    print("IMC:",("%.2f"%i),"\nSituacao: Abaixo do peso")
elif 20>=i<25:
    print("IMC:",("%.2f"%i) ,"\nSituacao: Peso Normal")
elif 25>=i<30:
    print("IMC:",("%.2f"%i),"\nSituacao: Acima do peso")
elif 30>=i<34:
    print("IMC:",("%.2f"%i),"\nSituacao: Obeso")
else:
    print("IMC:",("%.2f"%i),"\nSituacao: Muito Obeso")