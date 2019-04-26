salário = int(input ("digite seu salário: "))
aumento = int(input ("digite o percentual do aumento: "))
n_s = salário + (salário * aumento / 100)

print('você recebeu um aumento de', aumento,'% no seu salário. A partir de hoje você receberá', n_s, 'reais')