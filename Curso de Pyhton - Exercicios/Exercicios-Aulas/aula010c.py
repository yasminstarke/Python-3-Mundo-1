# Condição composta

n1 = float(input('Digite a primeira nota: ').replace(',','.'))
n2 = float(input('Digite a segunda nota: ').replace(',','.'))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m>= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

## OU  Condição simplicaficada

'''n1 = float(input('Digite a primeira nota: ').replace(',','.'))
n2 = float(input('Digite a segunda média: ').replace(',','.'))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS!!' if m>= 6.0 else 'Estude mais!')'''