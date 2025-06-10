# Mensagem de boas-vindas com seu nome
print("Bem vindo à Livraria do Paulo Ricardo Aranha")
print("------------------------------------------------")
print("--------------- MENU PRINCIPAL ------------------")

# Lista que armazenará os livros
lista_livro = []

# ID global para cada novo livro
id_global = 0

# Função para cadastrar um livro
def cadastrar_livro(id):
    print("--------------- MENU CADASTRAR LIVRO ------------------")
    print(f"Id do livro: {id}")
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)

# Função para consultar livros
def consultar_livro():
    while True:
        print("--------------- MENU CONSULTAR LIVRO ------------------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por id")
        print("3 - Consultar Livro(s) por autor")
        print("4 - Retornar")
        opcao = input(">>")

        if opcao == "1":
            for livro in lista_livro:
                print("---------------")
                print(f"id: {livro['id']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"editora: {livro['editora']}")
            print("---------------")
        elif opcao == "2":
            try:
                id_busca = int(input("Digite o id do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro["id"] == id_busca:
                        print("---------------")
                        print(f"id: {livro['id']}")
                        print(f"nome: {livro['nome']}")
                        print(f"autor: {livro['autor']}")
                        print(f"editora: {livro['editora']}")
                        print("---------------")
                        encontrado = True
                if not encontrado:
                    print("Livro não encontrado.")
            except:
                print("ID inválido.")
        elif opcao == "3":
            autor_busca = input("Digite o autor do(s) livro(s): ")
            encontrado = False
            for livro in lista_livro:
                if livro["autor"].lower() == autor_busca.lower():
                    print("---------------")
                    print(f"id: {livro['id']}")
                    print(f"nome: {livro['nome']}")
                    print(f"autor: {livro['autor']}")
                    print(f"editora: {livro['editora']}")
                    encontrado = True
            if not encontrado:
                print("Nenhum livro encontrado para este autor.")
            print("---------------")
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

# Função para remover livro
def remover_livro():
    print("--------------- MENU REMOVER LIVRO ------------------")
    while True:
        try:
            id_remove = int(input("Digite o id do livro a ser removido: "))
            for livro in lista_livro:
                if livro["id"] == id_remove:
                    lista_livro.remove(livro)
                    print("Livro removido com sucesso!")
                    return
            print("Id não encontrado. Tente novamente.")
        except:
            print("Valor inválido. Tente novamente.")

# Menu principal
while True:
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")
    opcao_menu = input(">>")

    if opcao_menu == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao_menu == "2":
        consultar_livro()
    elif opcao_menu == "3":
        remover_livro()
    elif opcao_menu == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida. Tente novamente.")