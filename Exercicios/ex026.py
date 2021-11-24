x=input('Digite uma frase:').strip().upper()
a= x.count('A')
print(f'Na frase a letra A aparece {a} vez(es)')
a1= x.find('A') +1
print(f'A primeira letra A apareceu na posição {a1} ')
a2= x.rfind('A') +1
print(f'A letra A aparece pela última vez na posição {a2}')


