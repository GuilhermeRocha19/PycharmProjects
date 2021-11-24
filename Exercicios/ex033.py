a=int(input('Digite o 1° valor:'))
b=int(input('Digite um 2° valor:'))
c=int(input('Digite o 3° valor:'))

menor = a
if b<a and b<c:
    menor = b
if c<a and b<c:
    menor = c

maior = a
if b>a and b>c:
    maior= b
if c>a and c>b:
    maior = c

    print(f'O maior valor digitado foi {maior}!')
    print(f'O menor valor digitado foi {menor}!')