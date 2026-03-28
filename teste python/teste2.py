import random

numero = random.randint(0, 10)
tentativa = 0

while tentativa != numero:
    tentativa = int(input('Digite um número de 1 a 10: '))
    
if tentativa < numero:
    print('Muito baixo!')
elif tentativa > numero:
    print('Muito alto!')
else:
    print('Acertou!')