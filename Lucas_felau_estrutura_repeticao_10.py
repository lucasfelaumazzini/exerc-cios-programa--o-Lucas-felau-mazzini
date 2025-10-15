#Programa que mostra os números inteiros entre dois valores

#Entrada dos números 
num1 = int(input("Digite o o primeiro número: "))
num2 = int(input("Digite o o segundo número: "))

#Garante que num1 seja o menor 
if num1 > num2:
    num1,num2 = num2,num1 #troca de posição 

#exibe os números no intervalo (sem incluir os extremos)
    print(f"Números entre {num1} e {num2}:")
    for i in range(num1 +1, num2):
        print(i)