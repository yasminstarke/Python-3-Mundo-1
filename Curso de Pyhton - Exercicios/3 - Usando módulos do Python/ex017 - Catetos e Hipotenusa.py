# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo,
# calcule e mostre o comprimento da hipotenusa.

# Fórmula ----->    c²=a²+b²

import math

a = int(input('Digite o comprimento do cateto oposto: '))
b = int(input('Digite o comprimento do cateto adjacente: '))

c = math.pow(a, 2) + math.pow(b, 2)
c2 = math.sqrt(c)

print('O valor da hipotenusa é de {}'.format(c2))

# OU

#import math

#a = int(input('Digite o comprimento do cateto oposto: '))
#b = int(input('Digite o comprimento do cateto adjacente: '))

#c = (math.pow(a, 2) + math.pow(b, 2))**(1/2)


#print('O valor da hipotenusa é de {}'.format(c))

