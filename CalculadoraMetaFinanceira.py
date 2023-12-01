# Função para calcular o número de meses para atingir uma meta financeira!
def calcular_meses(meta, poupanca):
    # Verifica se a meta e a poupança são números positivos!
    if isinstance(meta, (int, float)) and isinstance(poupanca, (int, float)) and meta > 0 and poupanca > 0:
        saldo = 0
        meses = 0

        while saldo < meta:
            saldo += poupanca
            meses += 1
        return meses
    else:
        return "Dados inválidos!"


# Looping para perguntar se o usuário deseja fazer outra simulação!
opcao = "s"

# Enquanto a opção for "s" ou "S"!
while opcao.lower() == "s":
    print("###########################################################################################################")
    print("Bem vindo(a) ao programa para calcular metas financeiras!")
    print("###########################################################################################################")

    # Pede ao usuário o valor da meta financeira!
    meta = True
    while meta is True:
        try:
            # Tenta converter a entrada do usuário em um número real!
            meta = float(input("Digite conforme exemplo o valor em R$ que deseja alcançar como meta: (ex: 1500.00): R$"))
        except ValueError:
            # Se ocorrer um erro de valor, exibe uma mensagem de erro!
            print("Valor inválido! Digite um número conforme o exemplo (ex: 1500.00).")

    # Pede ao usuário o valor que pode poupar por mês!
    poupanca = True
    while poupanca is True:
        try:
            # Tenta converter a entrada do usuário em um número real!
            poupanca = float(input("Digite conforme exemplo o valor em R$ que pode poupar por mês: (ex: 100.00): R$"))
        except ValueError:
            # Se ocorrer um erro de valor, exibe uma mensagem de erro!
            print("Valor inválido! Digite um número conforme o exemplo (ex: 1500.00).")

    # Calcula o número de meses para atingir a meta financeira usando a função calcular_meses!
    meses = calcular_meses(meta, poupanca)

    # Exibi o resultado no console!
    print("###########################################################################################################")
    print(f"Você vai levar {meses} meses para atingir a sua meta financeira.")
    print("###########################################################################################################")
    # Pergunta ao usuário se quer fazer outra simulação!
    opcao = input("Deseja fazer outra simulação? (s/n): ")

# Exibe uma mensagem de despedida!
print("Obrigado por usar a calculadora de meta financeira!")
