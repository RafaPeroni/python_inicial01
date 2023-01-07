# Programa em Pynthon para reforçar os operadores matemáticos

A = int(input('Digite um número para preencher o primeiro valor : '))
# para interagir com o usuário podemos usarf o "input", tipamos ele para a forma a qual
# iremos utilizar e o mesmo receberá aquele tipo de infomação
B = int(input('Diggite um número para preencher o segundo valor : '))
# OPERADOR DE SOMA
soma = A + B

# OPERADOR DE SUBTRAÇÃO
subtracao = A - B

# OPERADOR DE DIVISÃO
divisao = A / B

# OPERADOR DE MULTIPLICAÇÃO
multiplicacao = A * B

# OPERADOR DE RESTO DA DIVISÃO
resto = A % B


print(type(soma))
# comando type revela a tipagem da variável

# MODELO_1 necessário trocar o tipo da váriável para poder concatenar (str) converte para string 1º FORMA
# print('soma          : ' + str(soma))
# print('subtracao     : ' + str(subtracao))
# print('divisao       : ' + str(divisao))
# print('multiplicação : ' + str(multiplicacao))
# print('resto divisão : ' + str(resto))
# print(' ')



# modelo 2_ Concatenante string e int em uma linha de código e exibindo em várias ".format()"
print('soma          : {soma} \nsubtração     : {sub} \ndivisão       : {divi} \nMultiplicação : {mult} \nResto divisão : {resto} '.format(soma=soma,sub=subtracao,divi=divisao,mult=multiplicacao,resto=resto))


