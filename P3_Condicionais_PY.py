# Este projeto se baseia em desenvolver o Condicionais usando o raciocínio lógico e Python

A = int(input("Digite um valor para a variável  'A' : "))
B = int(input("Digite um valor para a variável  'B' : "))
C = int(input("Digite um valor para a variável  'C' : "))

# operadores lógicos 'if','else' e 'elif'
# operadores condicionais '==','and' e 'or'

if A > B and A > C:
    print("A variável 'A' tem o maior valor {} ".format(A))
elif B > A and B > C:
    print("A variável 'B' tem o maior valor {} ".format(B))
else:
    print("A variável 'C' tem o maior valor {} ".format(C))

print("Fim algoritimo 1")

if A + B > 100 or A + C > 100 or B + C > 100:
    print('A soma de duas quaisquer variáveis ultrapassa a marca de 100 pontos')
elif A - B < 0 or A - C < 0 or B - C < 0:
    print('A subtração de duas quaisquer variáveis é inferior a marca de 0 pontos')
else:
    print('a soma ou a subtração de duas quaisquer variáveis fica entre uma pontuação de 0 e 100')
print('Fim algoritimo 2')
