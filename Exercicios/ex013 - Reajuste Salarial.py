# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

s = float(input("Digite seu salário atual: R$").replace(',', '.'))

rs = ((s * (15 / 100)) + s)

print("Seu novo salário com reajuste de 15% é de R${:.3f}".format(rs))

# Outra forma de se fazer

#salário = float(input('Qual é o salário do Funcionário? R$').replace(',', '.'))
#novo = salário + (salário * 15 / 100)

#print('Um funcionário que ganhava R${:.3f}, com 15% de aumento, passa a receber R${:.3f}'.format(salário, novo))
