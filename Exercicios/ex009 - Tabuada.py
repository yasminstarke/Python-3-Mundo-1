# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

tab = int(input('Digite seu número para ver a Tabuada: '))

r0 = tab*0
r1 = tab*1
r2 = tab*2
r3 = tab*3
r4 = tab*4
r5 = tab*5
r6 = tab*6
r7 = tab*7
r8 = tab*8
r9 = tab*9
r10 = tab*10

print('{}x0 = {}\n{}x1 = {}\n{}x2 = {}\n{}x3 = {}\n{}x4 = {}\n{}x5 = {}\n{}x6 = {}\n{}x7 = {}\n'
      '{}x8 = {}\n{}x9 = {}\n{}x10 = {}'.format(tab,r0,tab,r1,tab,r2,tab,r3,tab,r4,tab,r5,tab,r6,tab,r7,tab,r8,tab,r9,tab,r10))

# Outro modo de fazer

#num = int(input('Digite um número para ver sua tabuada: '))

#print('-'*12)
#print('{} x {:2} = {}'.format(num, 1, num*1))
             #{:2} para deixar todos com 2 digitos
#print('{} x {:2} = {}'.format(num, 2, num*2))
#print('{} x {:2} = {}'.format(num, 3, num*3))
#print('{} x {:2} = {}'.format(num, 4, num*4))
#print('{} x {:2} = {}'.format(num, 5, num*5))
#print('{} x {:2} = {}'.format(num, 6, num*6))
#print('{} x {:2} = {}'.format(num, 7, num*7))
#print('{} x {:2} = {}'.format(num, 8, num*8))
#print('{} x {:2} = {}'.format(num, 9, num*9))
#print('{} x {:2} = {}'.format(num, 10, num*10))
#print('-'*12)