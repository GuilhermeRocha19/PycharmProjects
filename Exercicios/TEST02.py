
from random import randint


n = int(input("\n Digite um número entre [ 0 - 5 ] \n -> "))

if not ( n >= 0 and n <= 5 ):
    print("\n Desculpe, mas o número não está entre 0 e 5 ")

else:

    r = randint(0, 5)


    if r == n:
        print("\n == PARABÉNS O SENHOR(A) GANHOU === ")
        print(" VOCÊ: {}".format(n))
        print(" MÁQUINA: {}".format(r))

    else:
        print("\n === DESCULPE O SENHOR(A) PERDEU === ")
        print(" VOCÊ: {}".format(n))
        print(" MÁQUINA: {}".format(r))
