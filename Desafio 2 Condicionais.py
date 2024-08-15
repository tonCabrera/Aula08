# # # - ***Desafio 2:  Condicionais***

# # # ***Sistema de Reservas de Hotel:***

# # # ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

# # # - *Cadastro de Cliente:*

# # # *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

nome_cliente_principal = []
idade_cliente_principal = []

nome1 = input("Digite o nome do cliente(principal):\n>>")
idade1 = input("Digite a idade do cliente(principal):\n>>")

nome_cliente_principal.append(nome1)
idade_cliente_principal.append(idade1)

nome2 = input("Digite o nome do cliente(principal):\n>>")
idade2 = input("Digite a idade do cliente(principal):\n>>")

nome_cliente_principal.append(nome2)
idade_cliente_principal.append(idade2)

nome3 = input("Digite o nome do cliente(principal):\n>>")
idade3 = input("Digite a idade do cliente(principal):\n>>")

nome_cliente_principal.append(nome3)
idade_cliente_principal.append(idade3)

# nome_cliente_principal = ["Ton","Vivi","Iara"]
# idade_cliente_principal = ["40","35","15"]

# - *Reservas de Quartos:*

print("\nCadastro do cliente:\n")
print("1. nome:",nome_cliente_principal[0],"idade:",idade_cliente_principal[0])
print("2. nome:",nome_cliente_principal[1],"idade:",idade_cliente_principal[1])
print("3. nome:",nome_cliente_principal[2],"idade:",idade_cliente_principal[2])


# ***O sistema deve oferecer 3 tipos de quartos:*** 
# ***"Simples", "Duplo" e "Luxo".***
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***

quarto = ['Simples', 'duplo', 'luxo']
precos = [100, 150, 250]

print("Quarto disponíveis para reserva:\n")
print("1.",quarto[0]," - R$ ",precos[0])
print("2.",quarto[1]," - R$ ",precos[1])
print("3.",quarto[2]," - R$ ",precos[2])

# ***Cada cliente deve escolher um quarto para sua estadia1.

nome_cliente_reserva = []
quarto_cliente_reserva = []
preco_cliente_reserva = []
estadia_cliente_reserva = []

cliente_reserva1 = input("\nSelecione o id cliente que ira reserva:\n")

if cliente_reserva1 == "1":
    nome_cliente_reserva.append(nome_cliente_principal[0])
elif cliente_reserva1 == "2":
    nome_cliente_reserva.append(nome_cliente_principal[1])
elif cliente_reserva1 == "3":
    nome_cliente_reserva.append(nome_cliente_principal[2])

quarto_reserva1 = input("\nSelecione o id do quarto para reserva:\n")

if quarto_reserva1 == "1":
    quarto_cliente_reserva.append(quarto[0])
    preco_cliente_reserva.append(precos[0])
elif quarto_reserva1 == "2":
    quarto_cliente_reserva.append(quarto[1])
    preco_cliente_reserva.append(precos[1])
elif quarto_reserva1 == "3":
    quarto_cliente_reserva.append(quarto[2])  
    preco_cliente_reserva.append(precos[2])  

estadia_reserva1 = input("\nQuantidade de dias da reserva:\n")
estadia_cliente_reserva.append(estadia_reserva1)


cliente_reserva2 = input("\nSelecione o id cliente que ira reserva2:\n")

if cliente_reserva2 == "1":
    nome_cliente_reserva.append(nome_cliente_principal[0])
elif cliente_reserva2 == "2":
    nome_cliente_reserva.append(nome_cliente_principal[1])
elif cliente_reserva2 == "3":
    nome_cliente_reserva.append(nome_cliente_principal[2])

quarto_reserva2 = input("\nSelecione o id do quarto para reserva:\n")

if quarto_reserva2 == "1":
    quarto_cliente_reserva.append(quarto[0])
    preco_cliente_reserva.append(precos[0])
elif quarto_reserva2 == "2":
    quarto_cliente_reserva.append(quarto[1])
    preco_cliente_reserva.append(precos[1])
elif quarto_reserva2 == "3":
    quarto_cliente_reserva.append(quarto[2])  
    preco_cliente_reserva.append(precos[2])  

estadia_reserva2 = input("\nQuantidade de dias da reserva:\n")
estadia_cliente_reserva.append(estadia_reserva2)


cliente_reserva3 = input("\nSelecione o id cliente que ira reserva3:\n")

if cliente_reserva3 == "1":
    nome_cliente_reserva.append(nome_cliente_principal[0])
elif cliente_reserva3 == "2":
    nome_cliente_reserva.append(nome_cliente_principal[1])
elif cliente_reserva3 == "3":
    nome_cliente_reserva.append(nome_cliente_principal[2])

quarto_reserva3 = input("\nSelecione o id do quarto para reserva:\n")

if quarto_reserva3 == "1":
    quarto_cliente_reserva.append(quarto[0])
    preco_cliente_reserva.append(precos[0])
elif quarto_reserva3 == "2":
    quarto_cliente_reserva.append(quarto[1])
    preco_cliente_reserva.append(precos[1])
elif quarto_reserva3 == "3":
    quarto_cliente_reserva.append(quarto[2])  
    preco_cliente_reserva.append(precos[2])  

estadia_reserva3 = input("\nQuantidade de dias da reserva:\n")
estadia_cliente_reserva.append(estadia_reserva3)


# - ***Cálculo da Estadia:***

print("\nCliente:", nome_cliente_reserva[0])
print("Reservou quarto:", quarto_cliente_reserva[0])
print("Estadoa: ",estadia_cliente_reserva[0])
print(f"Total da reserva:{float(preco_cliente_reserva[0]) * float(estadia_cliente_reserva[0])}")

print("\nCliente:", nome_cliente_reserva[1])
print("Reservou quarto:", quarto_cliente_reserva[1])
print("Estadoa: ",estadia_cliente_reserva[1])
print(f"Total da reserva:{float(preco_cliente_reserva[1]) * float(estadia_cliente_reserva[1])}")

print("\nCliente:", nome_cliente_reserva[2])
print("Reservou quarto:", quarto_cliente_reserva[2])
print("Estadoa: ",estadia_cliente_reserva[2])
print(f"Total da reserva:{float(preco_cliente_reserva[2]) * float(estadia_cliente_reserva[2])}")

# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***
# Exemplo: 

#  ***valor_cliente3 = preco_duplo * cliente3_dias***

# *Pagamento:*

# *O sistema deve exibir o valor total a ser pago por cada cliente após a aplicação do desconto.*