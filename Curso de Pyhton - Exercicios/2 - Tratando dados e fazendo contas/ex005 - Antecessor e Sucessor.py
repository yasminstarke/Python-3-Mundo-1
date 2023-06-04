# Faça um programa que leia um número Inteiro e mostre na tela o
# seu sucessor e antecessor.

# Usando 3 variaveis (n,a,s)

n = int(input('Seja bem vindo, digite um número: '))
a = n-1
s = n+1
print('>>> O seu antecessor é o número:  {} \n >>> O seu sucessor é o número:  {}'.format(a,s))



# Podemos fazer o mesmo programa apenas com 1 variavel (n)

# n = int(input('Seja bem vindo, digite um número: '))
# print('>>> O seu antecessor é o número:  {} \n >>> O seu sucessor é o número:  {}'.format(n, (n-1), (n+1)))

# Quanto menos váriaveis mais memoria irá economizar do seu dispositivo.
# Se mais pra frente você precisar do antecessor e sucessor terá de criar váriaveis, se não for não precisa.
