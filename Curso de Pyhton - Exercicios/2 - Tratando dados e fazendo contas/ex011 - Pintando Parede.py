# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a
# sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

a = float(input("Digite a altura da parede: ").replace(',','.'))
l = float(input('Digite o largura da parede: ').replace(',','.'))

area = (a*l)/2

print("Para pintar essa parede serão necessários {:.1f} litros".format(area))

# Outra maneira de fazer

#larg = float(input("Largura da parede: ").replace(',','.'))
#alt = float(input("Altura da parede: ").replace(',',"."))
#área = larg * alt

#print("Sua parede tem a dimensão de {}m x {}m e sua área é de {}m².".format(larg, alt, área))

#tinta = área / 2

#print("Para pintar essa parede, você precisará de {}l de tinta.".format(tinta))

