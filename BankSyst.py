# Para saber as personalizações da minha IDE, vide README.md no repositório anninyia.

#---------------------------------------------------------------------------------------------------------------------------#

# ! leia README.md para mais detalhes sobre o projeto
# ? Implementar um sistema de gerente !

#---------------------------------------------------------------------------------------------------------------------------#

import json
import random
from datetime import datetime

# Função para carregar dados do arquivo json 
def carregar_dados():
    try:
        with open('contas.json', 'r') as arquivo: # Abre o arquivo json
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError): # Se não achar, retorna com erro e encerra o programa
        return []

# Função para salvar dados no arquivo json
def salvar_dados(contas):
    with open('contas.json', 'w') as arquivo:
        json.dump(contas, arquivo, indent=4)

# ------------------------------- SISTEMA Create, Update, Read, Delete (CRUD) ------------------------------- #

# Função para criar uma nova conta (CREATE)
def criar_conta(): 
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite seu CPF(XXX.XXX.XXX-XX): ")
    
    # Gerar número de conta aleatório com 6 dígitos(o usuário não criará o número de conta)
    
    numero_conta = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    
    # Gerar PIN aleatório com 4 dígitos(o usuário não criará o PIN único, mas pode alterá-lo)

    pin = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    
    saldo = float(input("Digite o saldo inicial: "))

    transacoes = []

    nova_conta = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "numero_conta": numero_conta,
        "pin": pin,
        "saldo": saldo,
        "transacoes": transacoes
    }

    
    contas.append(nova_conta)
    salvar_dados(contas)

    print("Conta criada com sucesso!")
    print(f"O número da sua conta é: {numero_conta}")
    print(f"Seu PIN é: {pin}")

# Função para ler a conta (READ)
def ler_conta(numero_conta):
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            return conta
    print(f"Conta com número {numero_conta} não encontrada.")
    return None

# Função para atualizar a conta (UPDATE) 
# // ATUALIZAR PIN DA CONTA, DATA DE NASCIMENTO E CPF
def atualizar_conta(numero_conta, pin):
    conta = ler_conta(numero_conta)
    if conta:
        pin_input = input("Digite o PIN para confirmar: ")
        if pin_input == pin:
            print("O que deseja atualizar?")
            print("1. Nome")
            print("2. Data de Nascimento")
            print("3. CPF")
            print("4. PIN")
            
            opcao = input("Opção: ")
            if opcao == "1":
                novo_nome = input("Digite o novo nome: ")
                conta["nome"] = novo_nome
                salvar_dados(contas)
                print("Nome atualizado com sucesso.")
            elif opcao == "2":
                nova_data_nascimento = input("Digite a nova data de nascimento: ")
                conta["data_nascimento"] = nova_data_nascimento
                salvar_dados(contas)
                print("Data de nascimento atualizada com sucesso.")
            elif opcao == "3":
                novo_cpf = input("Digite o novo CPF: ")
                conta["cpf"] = novo_cpf
                salvar_dados(contas)
                print("CPF atualizado com sucesso.")
            elif opcao == "4":
                novo_pin = input("Digite o novo PIN: ")
                conta["pin"] = novo_pin
                salvar_dados(contas)
                print("PIN atualizado com sucesso.")
            else:
                print("Opção inválida.")
        else:
            print("PIN incorreto.")
    else:
        print("Conta não encontrada.")

# * Função para deletar a conta (DELETE)
def deletar_conta():
    numero_conta = input("Digite o número da conta que deseja deletar: ")
    pin = input("Digite o PIN para confirmar a exclusão: ")
    
    for indice, conta in enumerate(contas):
        if conta["numero_conta"] == numero_conta and conta["pin"] == pin:
            confirmacao = input("Tem certeza que deseja deletar a conta? (S/n): ")
            if confirmacao.upper() == "S":
                del contas[indice]
                salvar_dados(contas)
                print("Conta deletada com sucesso! Reinicialize o software para utilizar novamente.")
                exit() # Encerra o programa
            else:
                print("Operação de exclusão cancelada.")
                return

    print("Conta não encontrada ou PIN incorreto.")


# ------------------------------- SISTEMA PRINCIPAL ------------------------------- #
# Função para autenticar o usuário no sistema
def autenticar_usuario():
    numero_conta = input("Digite o número da conta: ")
    pin = input("Digite o PIN: ")

    conta = ler_conta(numero_conta)
    if conta and conta['pin'] == pin:
        return conta
    else:
        print("Número da conta ou PIN incorretos. Tente novamente.")
        return None

# Função para realizar um saque
def sacar(conta):
    valor = float(input("Digite o valor a sacar: "))
    if valor <= 0:
        print("Valor inválido.")
        return
    
    if conta["saldo"] < valor:
        print("Saldo insuficiente.")
        return
    
    conta["saldo"] -= valor
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Captura a data e hora atual para armazenar no JSON e depois mostrar no extrato
    
    if "transacoes" not in conta:
        conta["transacoes"] = []

    conta["transacoes"].append({"tipo": "Saque", "valor": -valor, "data": agora})
    salvar_dados(contas)
    print("Saque realizado com sucesso.")

# Função para realizar um depósito 
def depositar(conta):
    valor = float(input("Digite o valor a depositar: "))
    if valor <= 0:
        print("Valor inválido.")
        return
    conta["saldo"] += valor
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conta["transacoes"].append({"tipo": "Depósito", "valor": valor, "data": agora})
    salvar_dados(contas)
    print("Depósito realizado com sucesso.")

# Função para realizar uma transferência -- transferir dinheiro de uma conta para outra
def transferir(conta_origem):
    numero_conta_destino = input("Digite o número da conta de destino: ")
    valor = float(input("Digite o valor a transferir: "))

    if valor <= 0:
        print("Valor inválido.")
        return

    conta_destino = None
    for conta in contas:
        if conta["numero_conta"] == numero_conta_destino:
            conta_destino = conta
            break

    if not conta_destino:
        print("Conta de destino não encontrada.")
        return

    if conta_origem["saldo"] < valor:
        print("Saldo insuficiente para transferência.")
        return

    print(f"\nVocê está transferindo R$ {valor:.2f} para a conta de {conta_destino['nome']} ({conta_destino['numero_conta']}).")
    confirmacao = input("Confirma esta transferência? (S/n): ")

    if confirmacao.upper() == "S":
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conta_origem["saldo"] -= valor
        conta_destino["saldo"] += valor
        conta_origem["transacoes"].append({
            "tipo": "Transferência enviada",
            "valor": -valor,
            "data": agora,
            "destino": conta_destino["numero_conta"]
        })
        conta_destino["transacoes"].append({
            "tipo": "Transferência recebida",
            "valor": valor,
            "data": agora,
            "origem": conta_origem["numero_conta"]
        })
        salvar_dados(contas)
        print("Transferência realizada com sucesso.")
    else:
        print("Transferência cancelada.")

# Função para consultar saldo -- exibe o saldo atual da conta
def consultar_saldo(conta):
    print(f"Seu saldo atual é: R$ {conta['saldo']}")

# Função para listar extratos -- transações e depósitos realizadas
def extrato(conta):
    if not conta.get("transacoes", []): 
        print("Você não realizou transações até o momento.")
    else:
        print("\nExtrato de Transações:")
        for transacao in conta["transacoes"]:
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            data = transacao["data"]
            if "destino" in transacao:
                destino = transacao["destino"]
                print(f"{data} - {tipo} de R${valor:.2f} para conta {destino}")
            elif "origem" in transacao:
                origem = transacao["origem"]
                print(f"{data} - {tipo} de R${valor:.2f} da conta {origem}")
            else:
                print(f"{data} - {tipo} de R${valor:.2f}")

# Função para exibir o menu inicial -- opções disponíveis para o usuário
def menu_inicial():
    print("Escolha uma opção:")
    print("1. Criar uma nova conta")
    print("2. Acessar uma conta existente")
    print("3. Sair")

# Função para exibir o menu principal -- opções disponíveis para o usuário
def exibir_menu():
    print("\n=== Menu ===")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Transferir")
    print("4. Consultar Saldo")
    print("5. Atualizar Conta")
    print("6. Deletar Conta")
    print("7. Gerar Extrato")
    print("8. Sair")

# Função principal
def main():
    global contas
    contas = carregar_dados()
    print("Bem-vindo ao Sistema Bancário\n")

    while True:
        menu_inicial()  # Exibir o menu inicial

        opcao = input("Opção: ")

        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            conta = autenticar_usuario()
            if conta:
                print(f"\n\t===== Bem vindo(a), {conta['nome']}! =====\nO que deseja realizar no momento?")
                while True:
                    exibir_menu()
                    opcao = input("Escolha uma opção: ")
                    if opcao == "1":
                        sacar(conta)
                    elif opcao == "2":
                        depositar(conta)
                    elif opcao == "3":
                        transferir(conta)
                    elif opcao == "4":
                        consultar_saldo(conta)
                    elif opcao == "5":
                        atualizar_conta(conta["numero_conta"], conta["pin"])
                    elif opcao == "6":
                        deletar_conta()
                    elif opcao == "7":
                        extrato(conta)
                    elif opcao == "8":
                        print("Obrigado por usar nosso sistema. Volte sempre!")
                        return
                    else:
                        print("Opção inválida.")
            else:
                print("Número da conta ou PIN incorretos. Tente novamente.")
        elif opcao == "3":
            print("Obrigado por usar nosso sistema. Volte sempre!")
            return
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
