#Programa que verifica que se um número é inteiro ou decimal

#Entrada
num = float(input("Digite um número: "))

#Verificação usando arredondamento
if num == round(num):
    print("O número é inteiro.")
else:
    print("O número é decimal.")