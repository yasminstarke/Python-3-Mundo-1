# Crie um programa que leia o nome completo de uma pessoa e mostre:
#    --> O nome com todas as letras maiúsculas
#    --> O nome com todas minúsculas
#    --> Quantas letras ao toodo (sem considerar espaços)
#    --> Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome....')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#format(len(nome) - nome.count(' ')) = quantos caracteres ao todos - o numero que espaços que ele encontrar, por isso o uso do .count(' ')
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#nome.find(' ') = encontre o primeiro espaço


#######      OUTRA FORMA    #############

'''nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome....')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#                                          quantos caracteres ao todo - o numero de espaços que ele encontrar, por isso o uso do .count(' ')
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0]))'''




