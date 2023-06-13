print('\033[1;31;42mOla, Mundo!\033[m')  # para fechar o código da cor é so acrescentar no final de onde você quer
                                        #     \033[m

#### OUTRA FORMA, colocando no .format ####

'''nome = 'Yasmin'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[1;31;42m', nome, '\033[m'))'''


### OUTRA FORMA ######

'''nome = 'Yasmin'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))'''
