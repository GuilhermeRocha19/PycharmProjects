x=float(input('Qual a distância da viagem em km?'))
vn= x*0.50
vp= x*0.45
if x>= 201:
    print(f'Você está prestes a começar uma viagem de {x}km \nE o preço da passagem será de R${vp}!')
else:
    print(f'Você está prestes a começar uma viagem de {x}km \nE o preço da passagem será de R${vn}!')