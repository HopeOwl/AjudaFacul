with open('Carros.txt') as Carros:
    f = Carros.readlines()
Carros = []
for i in f:
    Carros.append(i[:-1])

with open('CarrosXCores.txt') as CarrosXCores:
    f = CarrosXCores.readlines()
CarrosXCores = []
for i in f:
    CarrosXCores.append(i[:-1])
vendas_FiatUno = 0
vendas_ChevroletChevette = 0
vendas_VWGol = 0
vendas_VWFusca = 0
vendas_ChevroletOpala = 0
for vendas in range(len(CarrosXCores)):
    if CarrosXCores[vendas][0] == '1':
        vendas_FiatUno += 1

for vendas in range(len(CarrosXCores)):
    if CarrosXCores[vendas][0] == '2':
        vendas_ChevroletChevette += 1

for vendas in range(len(CarrosXCores)):
    if CarrosXCores[vendas][0] == '3':
        vendas_VWGol += 1

for vendas in range(len(CarrosXCores)):
    if CarrosXCores[vendas][0] == '4':
        vendas_VWFusca += 1

for vendas in range(len(CarrosXCores)):
    if CarrosXCores[vendas][0] == '5':
        vendas_ChevroletOpala += 1

print(f'Vendas Fiat Uno = {vendas_FiatUno}\n'
      f'Vendas Chevrolet Chevette = {vendas_ChevroletChevette}\n'
      f'Vendas VW Gol = {vendas_VWGol}\n'
      f'Vendas VW Fusca = {vendas_VWFusca}\n'
      f'Vendas Chevrolet Opala = {vendas_ChevroletOpala}\n')
