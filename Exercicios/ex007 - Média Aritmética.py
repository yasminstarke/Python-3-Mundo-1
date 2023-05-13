# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite a 1ª nota: ').replace(',','.'))
n2 = float(input('Digite a 2ª nota: ').replace(',','.'))
m = float((n1+n2)/2)
print('O valor da sua média é {:.1f}'.format(m))

# Outra maneira sem substituir virgula por ponto

#n1 = float(input('Digite a 1ª nota: '))
#n2 = float(input('Digite a 2ª nota: '))
#m = float((n1+n2)/2)
#print('O valor da sua média é {:.1f}'.format(m))