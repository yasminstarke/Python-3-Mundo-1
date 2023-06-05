# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo,
# calcule e mostre o comprimento da hipotenusa.

# Fórmula ----->    c²=a²+b²

import math

a = float(input('Digite o comprimento do cateto oposto: ').replace(',','.'))
b = float(input('Digite o comprimento do cateto adjacente: ').replace(',','.'))

c = math.pow(a, 2) + math.pow(b, 2)
c2 = math.sqrt(c)

print('O valor da hipotenusa é de {:.2f}'.format(c2))

# OU

'''import math

a = float(input('Digite o comprimento do cateto oposto: ').replace(',','.')
b = float(input('Digite o comprimento do cateto adjacente: ').replace(',','.')
c = (math.pow(a, 2) + math.pow(b, 2))**(1/2)

print('O valor da hipotenusa é de {}'.format(c))'''


# OU

'''co = float(input('Comprimento do cateto oposto: ').replace(',','.'))
ca = float(input('Comprimento do cateto adjacente: ').replace(',','.'))
hi = (co ** 2 + ca **2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))'''

# OU

'''import math

co = float(input('Comprimento do cateto oposto: ').replace(',','.'))
ca = float(input('Comprimento do cateto adjacente: ').replace(',','.'))
hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f}'.format(hi))'''
