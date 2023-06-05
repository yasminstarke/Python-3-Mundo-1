# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Exemplo: Digite um número: 6.127
#          O número 6.127 tem a parte Inteira 6.

from math import trunc

num = float(input("Digite um número: ").replace(',','.'))
inteiro = trunc(num)

print('O número {} tem a parte Inteira {}'.format(num, inteiro))

#### OUTRA FORMA DE SE FAZER - Só retirar as ''' do inicio e fim que o código funciona.

'''from math import trunc

num = float(input('Digite um valor: ').replace(',','.'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))'''

############## OUTRA FORMA DE FAZER ###############

'''num = float(input('Digite um valor: ').replace(',','.'))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))'''

