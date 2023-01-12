# Este algoritimo tem como objetivo mostrar a funcionalidade de conjuntos

prss = str(input('Digite (s) para dar início a um algorítimo que te gera dois '
                 'copnjuntos aleatrórios e mais alguns detalhes :'))

if prss == 's':

# importando método ja existente pra facilitar a vida
    import random
# criando conjuntos
    v = {0}
    t = {0}

# loop para preencher os conjuntos
    for x in range(10):
        x += 1
# gerando e preenchendo números aleatórios nos conjuntos
        aleatorios = random.randint(1, 50)
        v.add(aleatorios)
        print(aleatorios)
        aleatorios = random.randint(1, 50)
        t.add(aleatorios)
        print(aleatorios)
        print(v, t)

# usando as funções para detalhas os conjuntos de formas diferentes
    # fazendo união(juntando todos os elementos que existem nos dois conjuntos
    conj1 = v.union(t)

    # fazendo interseção( juntando somente o que se repete nos dois conjuntos)
    conj2 = t.intersection(v)

    # fazendo a diferença do primeiro conjunto com o segundo(mostrando todos
    # os elementos que existem no primeiro e não no segundo)
    conj3 = v.difference(t)

    # fazendo a diferença do segundo conjunto com o primeiro(mostrando todos
    # os elementos que existem no primeiro e não no segundo)
    conj4 = t.difference(v)

    # fazendo a junçaõ de tudo que existe apenas no primeiro conjunto e
    # tudo que existe apenas no segundo conjunto
    conj5 = v.symmetric_difference(t)

# exibindo detalhe dos conjuntos
    print('\n união ={}'.format(conj1))
    print('\n interceção ={}'.format(conj2))
    print('\n diferença do primeiro conjunto com o segundo{}'.format(conj3))
    print('\n diferença do segundo conjunto com o primeiro{}'.format(conj4))
    print('\n diferença simétrica entre segundo e o primeiro conjunto{}'.format(conj5))

else:
    print("\nMas que pena, espero que na próxima eu possa despertar mais o seu interesse")





