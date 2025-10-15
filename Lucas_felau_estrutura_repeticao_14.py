#Inicializa contadores
pares = 0
impares = 0

#Loop para pedir 10 números
for i in range(10):
    numero = int(input(f"Digite o {i+1}° número: "))

if numero % 2 == 0:
    pares += 1
else:
    impares += 1

    #Exibe os resultados 
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")