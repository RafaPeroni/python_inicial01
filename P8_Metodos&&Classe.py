# Este algoritmo tem como ibjetivo mostrar algumas funcionalidades básicas de metodos e funções


# criamos uma classe intuitiva
class Multiplo:
    # criamos uma classe intuitiva
    def __init__(self, numveri):
        self.numb = numveri

    # criamos um método para criar uma função  de verificação
    def mult2(self):
        # fazemos uma verificação de multiplicidade e retornamos um valor conforme a condicional
        if self.numb % 2 == 0:
            return 'sim'
        else:
            return 'não'

    def mult3(self):
        if self.numb % 3 == 0:
            return 'sim'
        else:
            return 'não'

    def mult4(self):
        if self.numb % 4 == 0:
            return 'sim'
        else:
            return 'não'

    def mult5(self):
        if self.numb % 5 == 0:
            return 'sim'
        else:
            return 'não'

    def mult6(self):
        if self.numb % 6 == 0:
            return 'sim'
        else:
            return 'não'

    def mult7(self):
        if self.numb % 7 == 0:
            return 'sim'
        else:
            return 'não'

    def mult8(self):
        if self.numb % 8 == 0:
            return 'sim'
        else:
            return 'não'

    def mult9(self):
        if self.numb % 9 == 0:
            return 'sim'
        else:
            return 'não'

    def mult10(self):
        if self.numb % 10 == 0:
            return 'sim'
        else:
            return 'não'


# recolhemos o valor para os parametros da classe
num = int(input('Digite um número para saber se ele é multiplo de 2 , 5 ou 10 '))
# atribuimos um parametro a classe e o valor da classe em uma variável para retornar as funções dos métodos
multiplos = Multiplo(num)

# retornamos os valores das funções
print('O número {num} é multiplo de 2?  "{mult2}"\n'
      'O número {num} é multiplo de 3?  "{mult3}"\n'
      'O número {num} é multiplo de 4?  "{mult4}"\n'
      'O número {num} é multiplo de 5?  "{mult5}"\n'
      'O número {num} é multiplo de 6?  "{mult6}"\n'
      'O número {num} é multiplo de 7?  "{mult7}"\n'
      'O número {num} é multiplo de 8?  "{mult8}"\n'
      'O número {num} é multiplo de 9?  "{mult9}"\n'
      'O número {num} é multiplo de 10? "{mult10}"'
      ''.format(num=num,
                mult2=multiplos.mult2(),
                mult3=multiplos.mult3(),
                mult4=multiplos.mult4(),
                mult5=multiplos.mult5(),
                mult6=multiplos.mult6(),
                mult7=multiplos.mult7(),
                mult8=multiplos.mult8(),
                mult9=multiplos.mult9(),
                mult10=multiplos.mult10(),
                ))
