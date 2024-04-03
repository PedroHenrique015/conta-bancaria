opcao = -1
saldo = 2000
limite_saque = 500
tentativas_saque = 3
historico_saque = []
historico_deposito = []
texto1 = "Bem vindo ao nosso sistema"

while opcao != 0:
    print(f"""
        ####### {texto1} #######

""")
    opcao = int(input("[1] Sacar\n[2] Extrato\n[3] Depositar\n[0] Sair\n: "))
    if opcao == 1:
        if tentativas_saque > 0:
            saque = float(input("Insira o valor de saque: "))
            if saque > limite_saque:
                print("Desculpe, o valor de saque excede o limite permitido.")
            elif saldo >= saque:
                saldo -= saque
                historico_saque.append(saque)
                print(f"O seu saque de R${saque:.2f} foi efetuado com sucesso, sobrou R${saldo:.2f} na sua conta para uso.")
                tentativas_saque -= 1

            else:
                print("Saldo insuficiente.")
        else:
            print("Você atingiu o limite de tentativas de saque.")
    elif opcao == 2:
        print("====================================")
        print("Seu extrato está sendo exibido...")
        print(f"Você tem R${saldo:.2f} na conta.")
        print("Histórico de saques:", historico_saque)
        print("Histórico de depósitos:", historico_deposito)
        print("====================================")
    
    elif opcao == 3:
            deposito = float(input("Insira o valor de depósito para a sua conta: "))
            if deposito > 0:
                saldo += deposito
                historico_deposito.append(deposito)
                print(f"Depósito em sua conta de R${deposito:.2f} efetuado com sucesso. Seu saldo atual é R${saldo:.2f}.")
            else:
                print("O valor de depósito precisa ser positivo.")
    elif opcao == 0:
        print("Obrigado pela escolha do banco. Até logo!")
    else:
        print("Opção inválida.")
