import math
co=float(input('Comprimento cateto oposto:'))
ca=float(input('Comprimento cateto adjacente:'))
hi=math.hypot(co,ca)
#hi= (co**2+ca**2)**(1/2)
#print(f'A hipotenusa vai medir {hi:.2f}.')
print(f'A hipotenusa vai medir {hi:.2}!')
