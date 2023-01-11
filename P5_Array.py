# Este algoritmo tem como objetivo mostrar a ultilização básica de listas


# O programa tem a função de recolher a quantidade de pessoas
# que participam na em uma mepresa como assalariádos
# e faz uma média do salário, revela quem tem o maior salário e
# quem tem o menor, mostrando os seus respectivos valores

listN = []
listS = []
nome = ''
salario = 0
contadorS = 0
play = 's'

# loop para dar a escolha de saida quando desejada
while play != 'n':
    contadorP = int(input('Digite a quantidade de pessoas que entrarão na média da empresa : '))

# usando o for para receber a quantidade de pessoas da empresa e gerar um loop para criar a lista
    for x in range(contadorP):
        x += 1

# criação da lista de nomes da empresa
        nome = str(input('Digite o  nome do usuário : '))
        listN.insert(len(listN), nome)

# criação da lista de salários da empresa
        salario = int(input('Digite o salário (sem os centavos) do usuário : '))
        print("\n")
        listS.insert(len(listS), salario)

# fazendo a média e imprimindo o cálculo feito
    somaS = sum(listS)
    media = somaS / contadorP
    print(f'A média salarial da empresa é de {media} reais\n'
          f'calculo usado : soma de salarios {somaS},'
          f'dividido pela quantidade de '
          f'funcionários {contadorP}'.format(media=media, somaS=somaS, contadorP=contadorP))

# recolhendo o maior valor, buscando sua posição na lista para achar seu respectivo dono
    salarioM = max(listS)
    numSM = listS.index(salarioM)
    NomeMaxS = listN[numSM]

# recolhendo o menor valor, buscando sua posição na lista para achar seu respectivo dono
    salarioMin = min(listS)
    numSMin = listS.index(salarioMin)
    NomeMinS = listN[numSMin]



    print('\nO Maior salário é de "{NomeMS}" com o valor de R${maxS}\n'.format(NomeMS=NomeMaxS, maxS=salarioM))
    print('\nO Menor salário é de "{NomeMinS}" com o valor de R${minS}\n'.format(NomeMinS=NomeMinS, minS=salarioMin))

    play = str(input('Deseja fazer uma Nova média ou Sair da aplicação : (s/n)'))
    if play == 'n':
        print('\n'
              '----------------------OBRIGADO POR USAR NOSSO ALGORITMO VOLTE SEMPRE----------------------'
              '\n')
    elif play == 's':
        print('\n'
              '----------------------OBRIGADO PELA PREFERÊNCIA DE NOSSO ALGORITMO ----------------------'
              '\n')
        listN = []
        listS = []
    else:
        while play != 's' or play != 'n':
            play = str(input('Por favor, Digite "s" para fazer uma nova avaliação : \n'
                             f'--------------------- ou --------------------- '
                             f'\n Digite "n" para sair desta aplicação : '))


