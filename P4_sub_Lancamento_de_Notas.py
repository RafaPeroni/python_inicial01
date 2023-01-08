# Este programa se baseia em uma plataforma de lançamento de notas,
# que tem como objetivo determinar se um indivíduo foi aprovado ou nãoem determinados critérios
print('Digite o nome do aluno e suas notas serão válidas apenas notas maiores \n'
      'que 0 e menores que 100 digite os números já arredondados \n')
nome = input('Informe o nome do indivíduo que será  : ')

A = int(input('Digite a pontuação na matéria A : '))
if A < 0 or A > 100:
    while A < 0 or A > 100:
        A = int(input('Digite a pontuação "VÁLIDA" na matéria A : '))

B = int(input('Digite a pontuação na matéria B : '))
if B < 0 or B > 100:
    while B < 0 or B > 100:
        B = int(input('Digite a pontuação "VÁLIDA" na matéria B : '))

C = int(input('Digite a pontuação na matéria C : '))
if C < 0 or C > 100:
    while C < 0 or C > 100:
        C = int(input('Digite a pontuação "VÁLIDA" na matéria C : '))

D = int(input('Digite a pontuação na matéria D : '))
if D < 0 or D > 100:
    while D < 0 or D > 100:
        D = int(input('Digite a pontuação "VÁLIDA" na matéria D : '))

E = int(input('Digite a pontuação na matéria E : '))
if E < 0 or E > 100:
    while E < 0 or E > 100:
        E = int(input('Digite a pontuação "VÁLIDA" na matéria E : '))

F = int(input('Digite a pontuação na matéria F : '))
if F < 0 or F > 100:
    while F < 0 or F > 100:
        F = int(input('Digite a pontuação "VÁLIDA" na matéria F : '))

G = int(input('Digite a pontuação na matéria G : '))
if G < 0 or G > 100:
    while C < 0 or G > 100:
        G = int(input('Digite a pontuação "VÁLIDA" na matéria G : '))

H = int(input('Digite a pontuação na matéria H : '))
if H < 0 or H > 100:
    while H < 0 or H > 100:
        H = int(input('Digite a pontuação "VÁLIDA" na matéria H : '))

media = (A + B + C + D + E + F + G + H) / 8

if media < 60:
    print("\n Infelizmente o aluno " + nome + " foi 'REPROVADO' na média geral com a pontuação de {}".format(media))
else:
    print("\n Felizmente o aluno " + nome + " foi 'APROVADO' na média geral com a pontuação de {}".format(media))
