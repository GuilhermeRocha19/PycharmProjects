n=input('Digite seu nome completo:').strip()

print(f'Seu nome com todas letras maiúsculas:{n.upper()}.')
print(f'Seu nome com todas letras minúsculas:{n.lower()}.')

print('Seu nome completo tem {} letras!'.format(len(n)-n.count(' ')))
x=n.split()
print(f'Seu primeiro nome tem {len(x[0])} letras.')

