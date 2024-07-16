numero = input('Informe um numero: ')

numero_pares = []
numero_impares = []


if (numero != 'int'):
    numero = int(numero)


for i in range(numero):
    if (i % 2 == 0 ):
        numero_pares.append(i)
    else:
        numero_impares.append(i)

print(f'numeros pares{numero_pares}\nnumeros impares{numero_impares}')

