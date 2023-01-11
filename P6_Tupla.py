# Este algoritmo tem como objetivo mostrar o funcionamento de uma tupla

# exercício baseia-se em : usar a tupla para armazenar a
# os detalhes de uma tabela de IMC e expor o resultado
# dependendo do caso específico


# Criando tupla
tupla_imc = ('abaixo do peso', 'no peso normal', 'acima do peso', 'obeso')

# Criando chave para loop while
dnv = ' '

while dnv != 'n':
    # recolhendo variáveis para fazer salculo e retoranar resultados
    nom = str(input('Digite o seu nome: '))
    pes = float(input('Digite o seu peso: '))
    # altura pedida em centímetros pois máscara ainda não foi criada
    alt = int(input('Digite em centímetros a sua altura: '))

    # calculando imc e formatando a altura para o calculo
    imc = pes / ((alt/100) ** 2)

    # Condicional para retorno de resposta
    if imc < 18.5:
        resultIMC = tupla_imc[0]
    elif 18.5 < imc < 25:
        resultIMC = tupla_imc[1]
    elif 25 < imc < 30:
        resultIMC = tupla_imc[2]
    else:
        resultIMC = tupla_imc[3]

    # Retorno de resultado, contendo o nome, resultado do imc e do calculo de imc.
    print('\n'
          'Com as informações recolhidas de {nome} foi constatado que vc está {iimc} com IMC DE {imc}'
          '\n'
          .format(iimc=resultIMC, nome=nom, imc=imc))

    # Recolhendo resposta da chave de loop
    dnv = str(input('Deseja fazer um novo calculo ? (s/n): '))

    # Condicional para determinar o loop
    if dnv == 's':
        print('\n'
              '----------------------OBRIGADO PELA PREFERÊNCIA DE NOSSO ALGORITMO ----------------------'
              '\n')
    elif dnv == 'n':
        print('\n'
              '----------------------OBRIGADO POR USAR NOSSO ALGORITMO VOLTE SEMPRE----------------------'
              '\n')
    else:
        while dnv != 's' or dnv != 'n':
            dnv = str(input('Por favor, Digite "s" para fazer uma nova avaliação : \n'
                            f'--------------------- ou --------------------- '
                            f'\n Digite "n" para sair desta aplicação : '))
