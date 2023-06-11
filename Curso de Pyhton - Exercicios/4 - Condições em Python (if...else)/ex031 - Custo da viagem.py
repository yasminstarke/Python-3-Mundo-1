# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200km e R$0,45 para viagens mais longas.

distância = float(input('Qual é a distância da sua viagem: ').replace(',','.'))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
viagem1 = distância * 0.50
viagem2 = distância * 0.45
if distância <= 200:
    print('Sua passagem custará R$ {:.2f}'.format(viagem1))
else:
    print('Sua passagem custará R$ {:.2f}'.format(viagem2))

### OUTRA FORMA ####

'''distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''