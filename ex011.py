# Faça um programa que
#   leia:
#     a largura e
#     a altura de uma parede em metros,
#   calcule:
#     a sua área e
#     a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro(L) de tinta, pinta uma área de 2m².
qbç = ('v')
print ('{:v^50}'.format(qbç))
print ('Claculadora de tinta para pintar parede')
ql = ('-')
print ('{:-^50}'.format(ql))
altura = float(input('Digite a Altura (em metros(m)): '))
largura = float(input('Digite a Largura (em metros(m)): '))
print ('{:-^50}'.format(ql))
area = (altura*largura)
tintArea = float('2')
litrosTinta = (area/tintArea)
print ('A quantidade de tinta necessária para pintar sua parede é de {} litros.'.format(litrosTinta))
rdp = ('^')
print ('{:^^50}'.format(qbç))
