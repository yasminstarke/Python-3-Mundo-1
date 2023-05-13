# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raíz quadrada.

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('Analisando o número {}, podemos concluir que: \n >> Seu dobro vale {} \n >> Seu triplo vale {} \n >> Sua raíz quadrada '
      'vale {:.2f}'.format(n, d, t, r))

# Outra forma de criar

#n= int(input('Digite um número: '))
#print('Analizando o número {}, podemos concluir que: \n >> Seu dobro vale {} \n >> Seu tripo vale {} \n >> '
#      '>> Sua raíz quadrada vale {}'.format(n, (n*2), (n*3), int(n**(1/2))))