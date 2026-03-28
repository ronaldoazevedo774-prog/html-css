texto = input('Digite uma palavra: ')
vogais = 'AEIOUaeiou'
contador = 0

for letra in texto:
    if letra.lower() in vogais:
        contador += 1
print(f'Quantidade de vogais: {contador}')