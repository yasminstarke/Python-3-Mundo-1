# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.

# Exemplo: Ana Maria de Souza
# Primeiro = Ana
# Último : Souza

n = str(input('Digite seu nome completo: ')).strip()
print('\nOlá {}!!'.format(n))
nome = n.split()
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
