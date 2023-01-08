# Este código servirá para aprensentar númeos impares

A = int(input('Digite um valor para ser analisado : '))
B = int(input('Digite um valor para ser analisado : '))
print("\n------------------- \n")
# modelo 1 identifica se uma variável é ímpar
if A % 2 == 0:
    print('Este número é Par {} '.format(A))
else:
    print('Este número é Ímpar {} '.format(A))

print('FIM ALGORITIMO MODELO 1')
print("\n------------------- \n")
if A % 2 == 0 and B % 2 == 0:
    print('os dois números são par ' + '"A" :{} '.format(A) + ' "B" :{}'.format(B))

elif A % 2 == 0 and B % 2 > 0:
    print('O valor da variável "A" é Par {} '.format(A))
    print('O valor da variável "B" é Ímpar {} '.format(B))
elif A % 2 > 0 and B % 2 == 0:
    print('O valor da variável "A" é Ímpar {} '.format(A))
    print('O valor da variável "B" é Par {} '.format(B))
else:
    print('os dois números são Ímpares ' + '"A" :{} '.format(A) + ' "B" :{}'.format(B))
print("\n------------------- \n")
print('FIM ALGORITIMO MODELO 2')