#Programa que lê três números e mostra o maior

#Entrada dos números
num1=float(input("Digite o primeiro número: "))
num2=float(input("Digite o segundo número: "))
num3=float(input("Digite o terceiro número: "))

#Verificação do maior número
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

#Saída do resultado
    print(f"O maior número é:{maior}")   