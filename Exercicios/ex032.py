import datetime
x1=datetime.date.today().year
x=int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))

if x==0:
    x= x1

if x % 4 ==0 and x % 100 != 0 or x % 400 == 0:
    print(f'{x} é um ano bissexto!')

else:
    print(f'{x} não é um ano bissexto!')




