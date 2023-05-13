# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.

n = input('Digite uma palavra: ')
print('Qual tipo primitivo desse valor? ', type(n))
print('É um número? ',n.isnumeric())
print('Só tem espaços?', n.isspace())
print('Está em maiúsculas? ', n.isupper())
print('Está em minúsculas? ', n.islower())
print('Está capitalizada? ', n.istitle())
print('É alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
