preço_produto = int(input ("digite o preço: "))
desconto = 5

desconto_produto = preço_produto - (preço_produto * desconto / 100)

print('você recebeu um desconto de', desconto,'% no seu produto')
print('preço a pagar de:', desconto_produto)
