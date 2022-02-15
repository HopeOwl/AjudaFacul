#Carregar arquivo Carros.txt
with open('Carros.txt') as Carros:
    Carros = Carros.readlines()

#Carregar arquivo CarrosXCores.txt
with open('CarrosXCores.txt') as CarrosXCores:
    CarrosXCores = CarrosXCores.readlines()

#Definir as variaveis de vendas de cada modelo de carro
vendas_FiatUno = 0
vendas_ChevroletChevette = 0
vendas_VWGol = 0
vendas_VWFusca = 0
vendas_ChevroletOpala = 0

#Ler a venda de cada modelo de carro e colocar na variavel criada acima
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

#Imprimir cada variavel na tela
print(f'Vendas Fiat Uno = {vendas_FiatUno}\n'
      f'Vendas Chevrolet Chevette = {vendas_ChevroletChevette}\n'
      f'Vendas VW Gol = {vendas_VWGol}\n'
      f'Vendas VW Fusca = {vendas_VWFusca}\n'
      f'Vendas Chevrolet Opala = {vendas_ChevroletOpala}\n')
