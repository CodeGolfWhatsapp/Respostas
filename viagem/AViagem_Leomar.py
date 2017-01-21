s=int(input('Informe a distancia em Km: '))
r=round(s/float(input('Informe o consumo medio: ')))
print('Total em Litros de combustivel: %d Litros\nTotal gasto com combustivel: R$ %.2f\nParadas previstas: %d'%(r,r*3.8,s/250))