# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

x = float(input('Digite o ângulo que deseja: ').replace(',','.'))

seno = math.sin(math.radians(x))
cosseno = math.cos(math.radians(x)) #Como usei import math, eu preciso referenciar o math.radians, math.cos, math.sin .....
tangente = math.tan(math.radians(x))

print('\nO ângulo {}° tem o valor de \n\nSeno = {:.2f} \nCosseno = {:.2f} \nTangente = {:.2f}'.format(x, seno, cosseno, tangente))

#OBS --> Como a medida é graus, precisamos converter para radianos usando math.radians()


################ OUTRA FORMA DE FAZER ####################

'''from math import radians, cos, sin, tan

ângulo = float(input('Digite o ângulo que você deseja: ').replace(',','.'))

seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))

cosseno = cos(radians(ângulo)) #Não preciso referenciar colocando math.radians. Coloco apenas radians, pois já está no comando from math import radians a referencia
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, seno))

tangente = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, seno))'''


#OBS --> Quuando eu uso from import eu não preciso referenciar o modulo/biblioteca que eu importei