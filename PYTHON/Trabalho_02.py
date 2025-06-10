# Exibe uma mensagem de boas-vindas com o nome e o cardápio
print("Bem-vindo à Loja de Gelados do Paulo Ricardo Aranha")
print("---------------------Cardápio---------------------")
print("--------------------------------------------------")
print("---| Tamanho |  Cupuaçu (CP)  |   Açaí (AC)     |---")
print("---|   P     |   R$ 9.00      |   R$ 11.00      |---")
print("---|   M     |   R$ 14.00     |   R$ 16.00      |---")
print("---|   G     |   R$ 18.00     |   R$ 20.00      |---")
print("--------------------------------------------------")

# Cria uma variável para somar o valor dos pedidos
total_pedido = 0

# Inicia o laço para aceitar pedidos
while True:
    # Pede o sabor ao usuário
    sabor = input("\nEntre com o sabor desejado (CP/AC): ").lower()

    # Verifica se o sabor é válido
    if sabor != "cp" and sabor != "ac":
        print("Sabor inválido. Tente novamente")
        continue

    # Pede o tamanho ao usuário
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").lower()

    # Verifica se o tamanho é válido
    if tamanho != "p" and tamanho != "m" and tamanho != "g":
        print("Tamanho inválido. Tente novamente")
        continue

    # Verifica o valor do item baseado no sabor e tamanho
    if sabor == "cp":
        if tamanho == "p":
            preco = 9.00
        elif tamanho == "m":
            preco = 14.00
        else:
            preco = 18.00
    else:  # sabor == "ac"
        if tamanho == "p":
            preco = 11.00
        elif tamanho == "m":
            preco = 16.00
        else:
            preco = 20.00

    # Mostra o item pedido e o valor
    nome_sabor = "Cupuaçu" if sabor == "cp" else "Açaí"
    print(f"Você pediu um {nome_sabor} no tamanho {tamanho.upper()}: R$ {preco:.2f}")

    # Soma ao total
    total_pedido += preco

    # Pergunta se deseja continuar
    mais = input("\nDeseja mais alguma coisa? (S/N): ").lower()
    if mais == "n":
        break

# Mostra o total final do pedido
print(f"\nO valor total a ser pago: R$ {total_pedido:.2f}")