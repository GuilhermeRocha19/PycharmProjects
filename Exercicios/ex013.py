a=int(input('Qual o salário do funcionário?'))
b=int(input('Quanto de aumento ele passará a ganhar?'))
v1= b / 100 * a
v2= v1 + a
print(f'O funcionário passará a receber R${v2} com os {b}% de aumento no salário!')