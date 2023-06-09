# Faça um programa que leia uma frase pelo teclado e mostre:
#       Quantas vezes aparece a letra "A"
#       Em que posição ela aparece a primeira vez
#       Em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')).strip().upper()
print('Sua frase tem {} letra(s) "A".'.format(frase.count('A')))
print('A primeira letra "A" aparece na {} posição.'.format(frase.find('A')+1))
print('A última letra "A" aparece na {} posição.'.format(frase.rfind('A')+1))
                  # Acrescento o +1 porque a contagem no python começa do zero, ai a contagem aparece certo para o usuário

