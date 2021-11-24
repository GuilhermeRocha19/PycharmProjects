r1=float(input('Tamanho da 1° reta:'))
r2=float(input('Tamanho da 2° reta:'))
r3=float(input('Tamanho da 3° reta:'))

if r1< r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('Formou um triângulo!')
else:
    print('Não forma um triângulo!')
