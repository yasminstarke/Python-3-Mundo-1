tempo = int(input("Quantos anos tem seu carro? "))  # Será executado SEMPRE, pois está colado ao lado esquerdo.
if tempo <=3:           #  SE
    print('Carro novo.')                         # toodo comando indentado para dentro PODE ou NÃO ser executado.
else:                   #   SENÃO
    print('Carro velho')
print('-- FIM --')

#### CONDIÇÃO SIMPLIFICADA ####

'''tempo = int(input('Quantos anos tem seu carro? '))
print("Carro novo" if tempo<=3 else "Carro velho")'''