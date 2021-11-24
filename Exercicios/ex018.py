import math
x=int(input('Digite o ângulo que você deseja:'))
s=(math.sin(math.radians(x)))
print(f"O seno do ângulo {x}° é {s:.2f}!")
c=math.cos(math.radians(x))
print(f'O cosseno do ângulo {x}° é {c:.2f}!')
t=math.tan(math.radians(x))
print(f'O tangente do ângulo {x}° é {t:.2f}!')