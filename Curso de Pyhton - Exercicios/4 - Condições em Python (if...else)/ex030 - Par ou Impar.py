# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

from time import sleep

n = int(input('Digite um número e te digo se ele é PAR ou ÍMPAR: '))
par = n % 2 == 0
if par:
    sleep(2)
    print('\nVocê digitou o número {}, ele é PAR.'.format(n))
else:
    sleep(2)
    print('\nVocê digitou o número {}, ele é ÍMPAR.'.format(n))

    ### OUTRA FORMA DE FAZER

'''from time import sleep

n = int(input('Digite um número e te digo se ele é PAR ou ÍMPAR: ')) % 2
if n == 0:
    sleep(2)
    print('\nVocê digitou o número {}, ele é PAR.'.format(n))
else:
    sleep(2)
    print('\nVocê digitou o número {}, ele é ÍMPAR.'.format(n))'''

## OUTRA FORMA

'''número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR.'.format(número))
else:
    print('O número {} é ÍMPAR.'.format(número))'''

