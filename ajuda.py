# Carregar arquivo Carros.txt
with open('Carros.txt') as Carros:
    Carros = Carros.readlines()

# Carregar arquivo CarrosXCores.txt
with open('CarrosXCores.txt') as CarrosXCores:
    CarrosXCores = CarrosXCores.readlines()

# Definir as variaveis de vendas de cada modelo de carro
vendas_FiatUno = 0
vendas_ChevroletChevette = 0
vendas_VWGol = 0
vendas_VWFusca = 0
vendas_ChevroletOpala = 0

# Ler a venda de cada modelo de carro e colocar na variavel criada acima
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

# Imprimir cada variavel na tela
print(f'Relatório 1 - Total de vendas por modelo de carro \n'
      f'Modelo                          Total\n'
      f'Fiat Uno                        {vendas_FiatUno}\n'
      f'Chevrolet Chevette              {vendas_ChevroletChevette}\n'
      f'VW Gol                          {vendas_VWGol}\n'
      f'VW Fusca                        {vendas_VWFusca}\n'
      f'Chevrolet Opala                 {vendas_ChevroletOpala}\n')

# Definir variavel de venda de carros vermelhos
venda_vermelhos = 0

# Ler as vendas de carros vermelhos
for i in range(len(CarrosXCores)):
    if CarrosXCores[i][2::] == 'Vermelho\n':
        venda_vermelhos += 1

# Imprimir as vendas de carros vermelhos
print(f'Relatório 2 - Total de vendas de carros de cor Vermelha \n'
      f'Cor                             Total\n'
      f'Vermelho                        {venda_vermelhos}\n')

# Declarar variavel de vendas de Chevrolet verde
vendas_ChevroletVerde = 0

# Ler as vendas das Chevrolet verdes
for vendas in range(len(CarrosXCores)):
    if CarrosXCores[vendas] == '2,Verde\n' or CarrosXCores[vendas] == '5,Verde\n':
        vendas_ChevroletVerde += 1

# Imprimir na tela a venda de Chevrolet verdes
print(f'Relatório 3 - Total de vendas de carros Chevrolet de cor Verde\n'
      f'Modelo          Cor             Total\n'
      f'Chevrolet       Verde           {vendas_ChevroletVerde}\n')

# Declarar variaveis de cada cor
Azul = 0
Vermelho = 0
Verde = 0
Branco = 0
Rosa = 0
Amarelo = 0
Preto = 0
Cinza = 0
Prata = 0

# Ler as vendas de cada cor
for i in range(len(CarrosXCores)):
    if CarrosXCores[i][2::] == 'Azul\n':
        Azul += 1
for i in range(len(CarrosXCores)):
    if CarrosXCores[i][2::] == 'Vermelho\n':
        Vermelho += 1
for i in range(len(CarrosXCores)):
    if CarrosXCores[i][2::] == 'Verde\n':
        Verde += 1
for i in range(len(CarrosXCores)):
    if CarrosXCores[i][2::] == 'Branco\n':
        Branco += 1
for i in range(len(CarrosXCores)):
    if CarrosXCores[i][2::] == 'Rosa\n':
        Rosa += 1
for i in range(len(CarrosXCores)):
    if CarrosXCores[i][2::] == 'Amarelo\n':
        Amarelo += 1
for i in range(len(CarrosXCores)):
    if CarrosXCores[i][2::] == 'Preto\n':
        Preto += 1
for i in range(len(CarrosXCores)):
    if CarrosXCores[i][2::] == 'Cinza\n':
        Cinza += 1
for i in range(len(CarrosXCores)):
    if CarrosXCores[i][2::] == 'Prata\n':
        Prata += 1

# Imprimir as vendas de cada cor na tela
print(f'Relatório 4 - Total de vendas de carros por cor\n'
      f'Cor                             Total\n'
      f'Amarelo                         {Amarelo}\n' 
      f'Azul                            {Azul}\n' 
      f'Branco                          {Branco}\n' 
      f'Cinza                           {Cinza}\n' 
      f'Prata                           {Prata}\n' 
      f'Preto                           {Preto}\n' 
      f'Rosa                            {Rosa}\n' 
      f'Verde                           {Verde}\n' 
      f'Vermelho                        {Vermelho}\n')
