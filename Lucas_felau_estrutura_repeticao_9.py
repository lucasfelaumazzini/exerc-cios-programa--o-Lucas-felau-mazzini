#Programa que mostra apenas os números ímpares entre 1 e 50

for i in range(1,51): #Vai de 1 até 50
    if i % 2 !=0: #Se o resto da divisão por 2 for diferente de 0, é ímpar
        print(i)