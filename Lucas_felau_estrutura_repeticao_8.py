#Programa que lê 5 números e mostra a soma e a média
soma = 0 #Variável para acumular a soma 

#Leitura dos 5 números
for i in range(1,6):
    num = float(input(f"Digite o {i}° número: "))
    soma += num #soma acumulada

#Cálculo da média
    media = soma /5

    #Saída dos resultados 
    print(f"A soma dos números é: {soma}")
    print(f"A média dos números é: {media}")