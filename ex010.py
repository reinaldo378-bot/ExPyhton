#Crie um programa que leia quanto dinheiro uma pessoa tem na certeira e mostre quantos Dólares ela pode comprar. Dólar hoje 01/09/25 - R$ 5,44
cbç = ('#')
print ('{:#^20}'.format(cbç))
print ('Carteira conversora Real (R$) para Dólar (US$).')
ql = ('=')
print ('{:=^20'.format(ql))
real = float(input('Digite o valor em Real você tem em carteira: '))
dolar = int(real/5,44)
print ('Voce pode compar {} US$'.format(dolar))
