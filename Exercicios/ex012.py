rs=int(input('Qual o preço do produto?'))
d=int(input('Quanto de desconto?'))
x= d / 100 * rs
VF= rs - x
print(f'O valor de R${rs} com {d}% de desconto, fica: R${VF}!')

