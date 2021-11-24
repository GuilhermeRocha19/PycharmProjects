import random
a=input('Digite um nome:')
b=input('Digite outro nome:')
c=input('Digite mais um nome:')
d=input('Digite um último nome')
l=[a,b,c,d]
r=random.choice(l)
print(f'O escolhido foi {r}...PARABÉNSS!')
