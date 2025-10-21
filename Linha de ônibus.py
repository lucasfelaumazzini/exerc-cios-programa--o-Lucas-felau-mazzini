# Definição de constantes e variáveis iniciais
LIMITE_MAXIMO = 50
linhas = []
linhas_sobrecarregadas = 0

# Definição da função de cadastro
def cadastrar_linha():
    numero = input("Digite o número da linha: ")
    nome = input("Digite o nome da linha: ")
    passageiros = int(input("Digite a quantidade de passageiros na hora de pico: "))

    # Verifica se está sobrecarregada
    sobrecarregada = passageiros > LIMITE_MAXIMO

    # Cria o registro da linha
    linha_criada = {
        "numero": numero,
        "nome": nome,
        "passageiros": passageiros,
        "sobrecarregada": sobrecarregada
    }

    return linha_criada


# Loop principal de cadastro
while True:
    print("\n--- Cadastro de Linha ---")
    linha_atual = cadastrar_linha()
    linhas.append(linha_atual)

    # Análise imediata
    if linha_atual["sobrecarregada"]:
        print(">> Linha sobrecarregada — adicionar mais ônibus.")
        linhas_sobrecarregadas += 1
    else:
        print(">> Linha com demanda normal.")

    continuar = input("\nDeseja cadastrar outra linha? (s/n): ").strip().lower()
    if continuar != "s":
        break


# Relatório Final
print("\n======= RELATÓRIO FINAL =======")
print(f"Total de linhas analisadas: {len(linhas)}")
print(f"Linhas sobrecarregadas: {linhas_sobrecarregadas}")

print("\nDetalhes das Linhas:")
for item in linhas:
    status_texto = "SOBRECARREGADA" if item["sobrecarregada"] else "Normal"
    print(f" - Linha {item['numero']} ({item['nome']}): {item['passageiros']} passageiros — {status_texto}")

print("\n======= FIM DO PROGRAMA =======")