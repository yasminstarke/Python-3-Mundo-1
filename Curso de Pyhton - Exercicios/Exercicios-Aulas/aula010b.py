# CONDIÇÃO SIMPLES ----> Quando tem apenas if

nome = str(input('Qual é seu nome? '))      # SEMPRE vai aparecer.
if nome == 'Yasmin':
    print('Que nome lindo você tem!')      # Só vai acontecer se o nome inserido for Yasmin
print('Bom dia, {}!'.format(nome))          # SEMPRE  vai aparecer.

# CONDIÇÃO COMPOSTA    ----> Quando tem else

'''nome = str(input('Qual é seu nome? '))
if nome == 'Yasmin':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))'''