import random

import time


print('---'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('---'*20)
time.sleep(0.5)
n=int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
time.sleep(2)

if n>= 6 :
    print("\n Desculpe, mas o número não está entre 0 e 5 ")
else:

    r = random.randint(0, 5)


    if n == r:
        print(f'PARABÉNS!! Você acertou! Eu pensei no número {r} e você no {n}!')
    else:
        print(f'ERROUU!Eu pensei no número {r} e você no {n}!')


