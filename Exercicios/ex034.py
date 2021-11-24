sal=float(input('Quanto é o valor do salário do funcionário?'))
a= 15/100
a1= a * sal + sal

b= 10/100
b1= b * sal + sal

if sal < 1500:
    print(f'O salário teve um aumento de \033[31m 15% \033[m, e passou a ser R${a1}!')
else:
    print(f'O salário teve um aumento de \033[32m 10% \033[m, e passou a ser R${b1}!')
