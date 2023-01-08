# Est algoritimo se basea na ultilização de laços de repetição


# Modelo 1 Verifica se o número digitado é primo usando "for"
num = int(input('Digite um número inteiro para saber se ele é Primo : '))
contador = 0
div = " "

for i in range(num):
    i += 1
    resto = num % i
    print(i, resto)
    if resto == 0:
        contador += 1
        div = div + ('  {}').format(i)


if contador > 2:
    print('numero não é primo {}'.format(num))
    print('Número divisível por outros {}'.format(contador) + ' números')
else:
    print('numero  é primo {}'.format(num))
    print('Número divisível por :')

print(div)
print('\n---------------------------\n')


# Modelo 2 Verifica se o número digitado é primo usando "while"
x = 0
div2 = ' '
contador2 = 0
while x < num:
    x +=1
    resto2= num % x
    print(x,resto2)

    if  resto2 == 0:
        contador2 += 1
        div2 = div2 + ('  {}').format(x)

if contador2 > 2 :
    print('numero não é primo {}'.format(num))
    print('Número divisível por outros {}'.format(contador2) + ' números')
else:
        print('numero  é primo {}'.format(num))
        print('Número divisível por :')

print(div)

