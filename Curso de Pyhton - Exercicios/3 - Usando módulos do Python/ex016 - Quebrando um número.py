# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Exemplo: Digite um número: 6.127
#          O número 6.127 tem a parte Inteira 6.

from math import trunc

num = float(input("Digite um número: ").replace(',','.'))
inteiro = trunc(num)

print('O número {} tem a parte Inteira {}'.format(num, inteiro))