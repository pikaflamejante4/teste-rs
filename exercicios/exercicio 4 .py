import os
os.system ("clear")

#Exercício 5
#Solicite que o usuário informe o valor de um produto e a forma de pagamento.
#1 - Pagamento à vista;
#2 - Pagamento à prazo.
#Se o produto for pago à vista aplique um desconto de 10% antes de mostrar o valor final, senão informe o mesmo
#valor do produto.
#Se for escolhida a opção de pagamento à prazo, solicite que o usuário digite a quantidade de parcelas que ele
#deseja pagar. Podendo parcelar em até 6 vezes.
#No final, mostre:
#Se o pagamento for à vista: 
#Valor do produto: R$ 100,00
#Forma de pagamento: à vista
#Valor do desconto: R$ 10,00
#Total a pagar: R$ 90,00
#Se o pagamento for à prazo: 
#Valor do produto: R$ 100,00
#Forma de pagamento: à prazo
#Quantidade de parcelas: 6
#Valor por parcela: R$ 16,66
#Total à prazo: R$ 100,00


valor_produto = float(input("Digite o valor do produto: "))
pagamento = (input("1 - Pagamento à vista;\n2 - Pagamento à prazo.\n\nDigite a opção desejada:"))


match pagamento:
    case "1":
        desconto = valor_produto * 0.10 
        total_pagar = valor_produto - desconto
        print("\n Detalhes de pagamento: ")
        print(f"Valor do produto: R$ {valor_produto: .2f}")
        print(f"Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto: .2f}")
        print(f"Total a pagar: R$ {total_pagar: .2f}")
    case "2":
        parcelas = int(input("Digite quantas vezes quer parcelar(ate 6x): "))

        match parcelas:
            case p if 1 <= p <= 6:
                valor_parcela = valor_produto / p
                print("\n Detalhes de pagamento: ")
                print(f"Valor do produto: R$ {valor_produto: .2f}")
                print(f"Forma de pagamento: a prazo")
                print(f"Quantidade de parcelas: {p}")
                print(f"Valor po parcelas: R$ {valor_parcela: .2f}")
                print(f"Total à prazo: R$ {valor_produto: .2f}")
            case _:
                print ("Número de parcelas inválidos, o máximo é ate 6x")
    case _:
        print("Opção inválida, escolha 1 para à vista ou 2 para à prazo!")
       
