# Crie um programa que leia quanto dinheiro tem na carteira e mostre quantos
# dólares ela pode comprar.           Considere $1,00 = R$4.99 e o €1 = R$5.55

carteira = float(input('Quanto dinheiro você tem na carteira?? R$').replace(',','.'))
                                                                    #.replace para substituir a vírgula por ponto
print('Com R${:.2f} você pode comprar US${:.2f}\nCom R${:.2f} você pode comprar €{:.2f}  '.format(carteira,
                                                                    carteira/4.99, carteira, carteira/5.55))


# Outra forma de fazer

#real = float(input('Quanto dinheiro você tem na carteira?? R$').replace(',','.'))
#dolar = float(real/3.27)
#print('Com R${} você pode comprar US${:.2}'.format(real, dolar))












