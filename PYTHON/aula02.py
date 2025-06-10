# Pede para o usuário digitar o valor de um produto
valor_unitario = float(input("Digite o valor unitário do produto: R$ "))
# Pede para o usuário digitar a quantidade de produtos
quantidade = int(input("Digite a quantidade desejada: "))
# Calcula o valor total sem aplicar desconto
valor_total_sem_desconto = valor_unitario * quantidade
# Verifica qual desconto deve ser aplicado de acordo com o valor total
if valor_total_sem_desconto < 2500:
    desconto = 0
elif valor_total_sem_desconto < 6000:
    desconto = 0.04
elif valor_total_sem_desconto < 10000:
    desconto = 0.07
else:
    desconto = 0.11
# Calcula o valor final com o desconto aplicado
valor_com_desconto = valor_total_sem_desconto * (1 - desconto)
# Mostra o valor antes do desconto
print(f"\nValor total sem desconto: R$ {valor_total_sem_desconto:.2f}")
# Mostra o percentual de desconto usado
print(f"Desconto aplicado: {desconto * 100:.0f}%")
# Mostra o valor final depois de aplicar o desconto
print(f"Valor total com desconto: R$ {valor_com_desconto:.2f}")
# Se o valor original foi igual ou acima de 2500, mostra mensagem de desconto
if valor_total_sem_desconto >= 2500:
    print("\nParabéns! Seu pedido recebeu um desconto especial.")
