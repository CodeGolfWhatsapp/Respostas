d=int(input('Informe a distancia em Km: '))
c=float(input('Informe o consumo medio: '))
l=round(d/c);g=l*3.8;p=d/250
print('Total de litros de combustivel: %d litros' % l)
print('Total gasto com combustivel: R$ %.2f' % g)
print('Paradas previstas: %d' % p)
