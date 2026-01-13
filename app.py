# =====================================================
# Sistema de Controle de Estoque - Loja de Eletrônicos
# =====================================================

estoque = {}


# ---------------- FUNÇÕES DE ENTRADA ----------------

def ler_nome_produto(mensagem):
    nome = input(mensagem).strip()
    if not nome:
        print("Erro: o nome do produto não pode estar vazio.")
        return None
    return nome


def ler_preco(mensagem):
    try:
        preco = float(input(mensagem))
        if preco <= 0:
            print("Erro: o preço deve ser maior que zero.")
            return None
        return preco
    except ValueError:
        print("Erro: informe um valor numérico válido.")
        return None


def ler_quantidade(mensagem):
    try:
        quantidade = int(input(mensagem))
        if quantidade < 0:
            print("Erro: a quantidade não pode ser negativa.")
            return None
        return quantidade
    except ValueError:
        print("Erro: informe um número inteiro válido.")
        return None


# ---------------- MENU PRINCIPAL ----------------

def exibir_menu():
    print("\n========= MENU DO SISTEMA =========")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Excluir produto")
    print("4 - Visualizar estoque")
    print("5 - Sair")
    print("==================================")


# ---------------- FUNCIONALIDADES ----------------

def adicionar_produto():
    nome = ler_nome_produto("Nome do produto: ")
    if nome is None:
        return

    if nome in estoque:
        print("Produto já cadastrado no estoque.")
        return

    preco = ler_preco("Preço do produto: ")
    if preco is None:
        return

    quantidade = ler_quantidade("Quantidade em estoque: ")
    if quantidade is None:
        return

    estoque[nome] = {
        "preco": preco,
        "quantidade": quantidade
    }

    print("Produto adicionado com sucesso!")


def atualizar_produto():
    nome = ler_nome_produto("Nome do produto a atualizar: ")
    if nome is None:
        return

    if nome not in estoque:
        print("Produto não encontrado no estoque.")
        return

    preco = ler_preco("Novo preço do produto: ")
    if preco is None:
        return

    quantidade = ler_quantidade("Nova quantidade em estoque: ")
    if quantidade is None:
        return

    estoque[nome]["preco"] = preco
    estoque[nome]["quantidade"] = quantidade

    print("Produto atualizado com sucesso!")


def excluir_produto():
    nome = ler_nome_produto("Nome do produto a excluir: ")
    if nome is None:
        return

    if nome in estoque:
        del estoque[nome]
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado no estoque.")


def visualizar_estoque():
    if not estoque:
        print("Estoque vazio.")
        return

    print("\n----------- ESTOQUE ATUAL -----------")
    for nome, dados in estoque.items():
        print(f"Produto: {nome}")
        print(f"Preço: R$ {dados['preco']:.2f}")
        print(f"Quantidade: {dados['quantidade']}")
        print("------------------------------------")


# ---------------- CONTROLE DO SISTEMA ----------------

def executar_sistema():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            excluir_produto()
        elif opcao == "4":
            visualizar_estoque()
        elif opcao == "5":
            print("Sistema encerrado com sucesso.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# ---------------- INICIALIZAÇÃO ----------------

executar_sistema()
