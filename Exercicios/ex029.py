x=float(input('Qual a velocidade atual do carro?'))
v= x-60
v2= v*7

if x >= 61:
    print(f'MULTADO! Você excedeu o limite permitido que é de 60km/h\nVocê deve pagar uma multa de R${v2}!')

print('Tenha um bom dia! Dirija com segurança! ')