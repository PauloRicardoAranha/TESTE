# Mostra uma mensagem de boas-vindas com o nome do desenvolvedor
print("Bem-vindo à Copiadora do Paulo Ricardo Aranha")

# Função que pergunta e valida o tipo de serviço
def escolha_servico():
    while True:
        print("\nEntre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        servico = input(">>").lower()

        if servico == "dig":
            return 1.10
        elif servico == "ico":
            return 1.00
        elif servico == "ipb":
            return 0.40
        elif servico == "fot":
            return 0.20
        else:
            print("Escolha inválida, entre com o tipo do serviço novamente")

# Função que pergunta e valida o número de páginas
def num_pagina():
    while True:
        try:
            paginas = int(input("Entre com o número de páginas: "))
            if paginas >= 20000:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente.")
                continue
            if paginas < 20:
                return paginas
            elif paginas < 200:
                return paginas * 0.85
            elif paginas < 2000:
                return paginas * 0.80
            else:
                return paginas * 0.75
        except:
            print("Valor inválido, digite apenas números inteiros.")

# Função que pergunta o serviço extra (encadernação)
def servico_extra():
    while True:
        print("\nDeseja adicionar algum serviço?")
        print("1 - Encadernação Simples - R$ 15.00")
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada")
        extra = input(">>")

        if extra == "1":
            return 15.00
        elif extra == "2":
            return 40.00
        elif extra == "0":
            return 0.00
        else:
            print("Opção inválida. Digite 0, 1 ou 2.")

# Código principal (main)
valor_servico = escolha_servico()
paginas_com_desconto = num_pagina()
valor_extra = servico_extra()

# Cálculo do total
total = (valor_servico * paginas_com_desconto) + valor_extra

# Mostra o resultado final
print(f"\nTotal: R$ {total:.2f} (serviço: {valor_servico:.2f} * páginas: {paginas_com_desconto:.0f} + extra: {valor_extra:.2f})")