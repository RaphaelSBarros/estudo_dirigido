import math

área = int(input('digite a área a ser pintada em m²:'))

litros_tinta = 1

cobertura = 6

lata = 18

preço_lata = 80

galão = 3.6

preço_galão = 25

quantidade_tinta = área / cobertura

print('quantidade de tinta a ser usada é de', quantidade_tinta, 'litros')

A = (quantidade_tinta / lata)
print('total de latas necessárias:', math.ceil (A))
print('total a pagar pela pintura usando somente lata é:', int(A * preço_lata))

B = (quantidade_tinta / galão)
print ('total de galões necessários:', math.ceil (B))
print ('total a pagar pela pintura usando somente galão é:', int(B * preço_galão))


C = (quantidade_tinta / (galão + lata))
print('total de latas e galões necessários:', math.ceil (C))
print('total a pagar pela pintura usando lata e galão é:', int(C * (preço_lata + preço_galão)))
