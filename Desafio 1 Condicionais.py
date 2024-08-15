# # - **Desafio 1 Condicionais***

# # ***Crie um sistema de e-commerce, onde o usuário possa:***

# # - ***cadastrar-se***
# cadastro = []

# nome = input("Digite seu nome:\n>>")
# cpf = input("Digite seu CPF:\n>>")
# endereco = input("Digite seu endereço:\n>>")
# email = input("Digite seu email:\n>>")
# telefone = input("Digite seu telefone:\n>>")

# cadastro = [nome, cpf, email, endereco, telefone]

# print("\nCadastro do cliente:\n")
# print("nome:",cadastro[0])
# print("cpf:",cadastro[1])
# print("email:",cadastro[2])
# print("endereco:",cadastro[3])
# print("telefone:",cadastro[4])

# # - ***comprar um produto***

# print("\nOlá,", cadastro[0])
# print("Seu cadastro foi realizado com sucesso!!!\n")

comprar = int(input("Digite '1' para realizar uma compra (ou '0' para finalizar).\n>>"))

if comprar == 1: 
    produtos = ['celular', 'computador', 'TV']
    precos = [1999.90, 2999.90, 3999.90]

    print("\nProdutos disponíveis em estoque:\n")
    print("1.",produtos[0]," - R$ ",precos[0])
    print("2.",produtos[1]," - R$ ",precos[1])
    print("3.",produtos[2]," - R$ ",precos[2])

# - ***descobrir o valor total***

    escolha1 = int(input("\nEscolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar):\n>>"))

    carrinho = []
    total = 0

    if escolha1 == 1:
        carrinho.append(produtos[0])
        total += precos[0]
    elif escolha1 == 2:
        carrinho.append(produtos[1])
        total += precos[1]
    elif escolha1 == 3:
        carrinho.append(produtos[2])
        total += precos[2]
    elif escolha1 == 0:
        comprar = 0

    if comprar == 1: 
        escolha2 = int(input("\nPara continuar comprando.\nEscolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar):\n>>"))

        if escolha2 == 1:
            carrinho.append(produtos[0])
            total += precos[0]
        elif escolha2 == 2:
            carrinho.append(produtos[1])
            total += precos[1]
        elif escolha2 == 3:
            carrinho.append(produtos[2])
            total += precos[2]
        elif escolha2 == 0:
            comprar = 0

    if comprar == 1: 
        escolha3 = int(input("\nPara continuar comprando.\n Escolha o número do produto que deseja adicionar ao carrinho (ou '0' para finalizar):\n>>"))

        if escolha3 == 1:
            carrinho.append(produtos[0])
            total += precos[0]
        elif escolha3 == 2:
            carrinho.append(produtos[1])
            total += precos[1]
        elif escolha3 == 3:
            carrinho.append(produtos[2])
            total += precos[2]  

# - ***pagar***
    print("\nVocê comprou:")
    if len(carrinho) > 0:
        print(carrinho)
        print(f"Total: R$ {total:.2f}")
    else:
        print("Nenhum produto comprado.")

else: 
    print("Até a proxima")