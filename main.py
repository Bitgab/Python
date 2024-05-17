import os
os.system("cls || clear")

"""
Descrição das variáveis:
  - quantidade_pares: Quantidade de números pares.
  - quantidade_impares: Quantidade de números ímpares.
  - quantidade_positivos: Quantidade de números positivos.
  - quantidade_negativos: Quantidade de números negativos.
  - maior_numero: O maior número.
  - menor_numero: O menor número.
  - media_pares: Média dos números pares.
  - media_impares: Média dos números ímpares.
  - media_geral: Média de todos os números.
  - numeros_invertidos: Os números na ordem inversa.
"""
# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = float('-inf')
menor_numero = float('inf')
soma_pares = 0
soma_impares = 0
soma_geral = 0
numeros = []

# Variáveis para armazenar os números
for i in range (1,6):
    numero = int (input(f"Digite o {i}ª número: ")) 
    numeros.append(numero)
    soma_geral += numero

# Processando números pares e ímpares
    if numero %2 == 0:
        soma_pares += numero
        quantidade_pares += 1

    else:
        soma_impares += numero
        quantidade_impares += 1
        
# Processando números positivo e negativo
    if numero > 0:
        quantidade_positivos += 1
    elif numero < 0: 
        quantidade_negativos += 1

# maior número e menor número
    if numero > maior_numero:
        maior_numero = numero

    if numero < menor_numero:
        menor_numero = numero
        
# Calculando as médias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / 5.0 
 

# Imprimindo as estatísticas
print("\nEstatísticas dos números: 5 números")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"O maior número: {maior_numero}")
print(f"O menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares}")
print(f"Média dos números ímpares: {media_impares}")
print(f"Média de todos os números: {media_geral}")
print(f"Números em ordem inversa:")
for indice, numero in enumerate(reversed(numeros), start=1):
    print(f"{len (numeros) -indice +1}ª número: {numero}")






