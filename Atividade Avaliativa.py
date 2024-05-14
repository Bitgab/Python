import os
os.system("cls || clear")

# Declarando as variáveis.
somaGeral = 0
somaPares = 0
somaImpares = 0
quantidadePares = 0
quantidadeImpares = 0
quantidadePositivo = 0
quantidadeNegativo = 0
maiorNumero = 0
menorNumero = float('inf')
numeros = [] 


for i in range(1,6):
    numero = int(input(f"Digite o {i}ª número: "))   
    numeros.append(numero)
    somaGeral += numero
    
    if numero %2 == 0:
        
        somaPares += numero
        quantidadePares += 1
        

    else: 
        
        somaImpares += numero
        quantidadeImpares += 1
        
        
# Positivo e Negativo.   
    if numero > 0:
        quantidadePositivo += 1
    else : 
        quantidadeNegativo += 1
# Maior e Menor número.
    if numero > maiorNumero:
        maiorNumero = numero

    elif numero < menorNumero:
        menorNumero = numero


    #maiorNumero = min(maiorNumero, numero)
    #menorNumero = max(menorNumero,numero)

# Cálculo das médias.
mediaPares = somaPares / quantidadePares
mediaImpares = somaImpares / quantidadeImpares
mediaGeral = somaGeral / 5.0

# Exibindo resultado.
print("\nEstatísticas dos números: 5 números")
print(f"Quntidade de pares: {quantidadePares}")
print(f"Quantidade de ímpares: {quantidadeImpares}")
print(f"Quantidade de positivo: {quantidadePositivo}")
print(f"Quantidade de negativo: {quantidadeNegativo}")
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
print(f"Média dos números pares: {mediaPares}")
print(f"Média dos números ímpares: {mediaImpares}")
print(f"Média de todos os números: {mediaGeral}")
print("\nNúmero em ordem inversa:")
for numero in reversed (numeros):
    print(f" {numero}",end="")