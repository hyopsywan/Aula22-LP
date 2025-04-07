# Atividade
# Estoque inicial
Estoque = {1: "sabao", 2: "esponja", 3: "pente"}
Produtos = {}

Opcao = 0
while Opcao != 3:
    print("\nMenu:")
    print("1 - Adicionar produto")
    print("2 - Consultar produto")
    print("3 - Sair")

    try:
        Opcao = int(input("Digite o número da opção que deseja: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        continue

    if Opcao == 1:
        nome_produto = input("Digite o nome do produto: ")
        try:
            quantidade = int(input("Digite a quantidade: "))
        except ValueError:
            print("Quantidade inválida. Digite um número inteiro.")
            continue

        if nome_produto in Produtos:
            Produtos[nome_produto] += quantidade
            print("Quantidade atualizada!")
        else:
            Produtos[nome_produto] = quantidade
            print("Produto adicionado!")

    elif Opcao == 2:
        nome_produto = input("Digite o nome do produto para consulta: ")
        if nome_produto in Produtos:
            print(f"Quantidade disponível: {Produtos[nome_produto]}")
        else:
            print("Produto não encontrado.")

    elif Opcao == 3:
        print("Saindo do sistema...")

    else:
        print("Opção inválida! Tente novamente.")