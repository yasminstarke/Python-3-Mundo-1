# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

p1 = float(input("Digite o preço do produto: R$ ").replace(',', '.'))

d = p1 * (5 / 100)
dt = p1 - d

print("O preço desse produto com 5% de desconto é R${:.2f}".format(dt))

# Outra forma de se fazer

#preço = float(input("Qual é o preço do produto? R$").replace(',', '.'))
#novo = preço - (preço * 5 / 100)

#print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
