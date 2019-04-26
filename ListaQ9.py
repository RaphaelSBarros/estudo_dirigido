cigarros_dia = int(input ("digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input ("digite o tempo fumado em anos: "))
minutos_perdidos_por_cigarro = 10
dias_perdidos = cigarros_dia * 365 * anos_fumando * 60 * minutos_perdidos_por_cigarro / 60 / 24

print('Você tem o total de', dias_perdidos, 'dias de vida perdidos por conta do cigarro')
