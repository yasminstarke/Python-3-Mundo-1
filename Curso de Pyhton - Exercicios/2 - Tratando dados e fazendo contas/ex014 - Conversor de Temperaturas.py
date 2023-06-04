# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

# Conversão de Celsius para Fahrenheit:
# F = (C * 9/5) + 32
# Onde F é a temperatura em Fahrenheit e C é a temperatura em Celsius.

# Conversão de Fahrenheit para Celsius:
# C = (F - 32) * 5/9
# Onde C é a temperatura em Celsius e F é a temperatura em Fahrenheit.

# Conversão de Celsius para Kelvin:
# K = C + 273.15
# Onde K é a temperatura em Kelvin e C é a temperatura em Celsius.

# Conversão de Kelvin para Celsius:
# C = K - 273.15
# Onde C é a temperatura em Celsius e K é a temperatura em Kelvin.

# Conversão de Fahrenheit para Kelvin:
# K = (F - 32) * 5/9 + 273.15
# Onde K é a temperatura em Kelvin e F é a temperatura em Fahrenheit.

# Conversão de Kelvin para Fahrenheit:
# F = (K - 273.15) * 9/5 + 32
# Onde F é a temperatura em Fahrenheit e K é a temperatura em Kelvin.
#
##################################### RESOLUÇÃO ##########################################################

c = float(input('Informe a temperatura em °C: ').replace(',','.'))
f = (c * 9/5) + 32

print("A temperatura {} °C, equivale a {} °F".format(c, f))

