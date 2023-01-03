from time import sleep

cart = []
# PRODUTOS
products = [{"id": 55, "name": 'Teclado Logitech', "price": 359.99, "amount": 1},
            {"id": 256, "name": 'Fone sem fio', "price": 150.00, "amount": 1},
            {"id": 541, "name": 'Iphone 16', "price": 20000.00, "amount": 1},
            {"id": 13, "name": 'Nokia', "price": 135.50, "amount": 1},
            {"id": 45, "name": 'Monitor 19"', "price": 700.00, "amount": 1},
            {"id": 698, "name": 'TV Samsung 4k 75"', "price": 5700.00, "amount": 1},
            {"id": 1243, "name": 'PC Gamer Gtx 1050Ti', "price": 5000.00, "amount": 1},
            {"id": 908, "name": 'Mouse Razzer', "price": 99.99, "amount": 1},
            {"id": 258, "name": 'Tablet CCE', "price": 450.00, "amount": 1},
            {"id": 157, "name": 'Copo stanley', "price": 300.00, "amount": 1}]
# INÍCIO
ecommerce = "E - C O M M E R C E"
do = "D O"
lukako = "L U K A K O"

def inicio():
    print("="*57)
    print(f"{ecommerce:^57}")
    print(f"{do:^57}")
    print(f"{lukako:^57}")
    print("="*57)
# MENU
def menu():
    sleep(0.2)
    print("="*57)
    sleep(0.2)
    print("1 - Adicionar um produto ao carrinho")
    sleep(0.2)
    print("2 - Remover um produto do carrinho")
    sleep(0.2)
    print("3 - Consultar valor do carrinho")
    sleep(0.2)
    print("4 - Sair do menu")
    sleep(0.2)
    while True:
        try:
            opcao = int(input("\033[0;33mEscolha uma das opções acima para continuar: \033[m"))
            break
        except ValueError:
            sleep(1)
            print(f"\033[0;31mDigite um número!\033[m")
    return opcao
# ADICIONAR UM PRODUTO
def adicionar_produto():
    print("="*57)
    sleep(1)
    print("\033[0;32mSegue abaixo uma lista dos nosso produtos disponíveis no estoque:\033[m")
    sleep(1)
    print("\033[0;33mNome                    Preço          Id\033[m")
    for produto in products:
        name = produto.get("name")
        price = produto.get("price")
        id = produto.get("id")
        sleep(0.2)
        print(f"{name:<23}", f"{price:<12.2f}", "(", f"{id}", ")")
    sleep(0.2)
    print("="*57)
    return_to_the_question = True
    while return_to_the_question == True:
        while True:
            try:
                sleep(1)
                product = int(input("\033[0;33mDigite o ID do produto que você deseja adicionar ao carrinho: \033[m"))
                break
            except ValueError:
                sleep(1)
                print(f"\033[0;31mDigite um número!\033[m")
        sleep(0.5)
        added = False
        tamanho = len(cart)
        contador = 1
        for produto in products:
            name = produto.get("name")
            ids = produto.get("id")
            if product == ids:
                sleep(1)
                if len(cart) == 0:
                    cart.append(produto)
                    print(f"\033[0;32m{name} adicionado ao carrinho!\033[m")
                    added = True
                    break
                else:
                    for produto_no_carrinho in cart:
                        if produto_no_carrinho["id"] == product:
                            if produto_no_carrinho["amount"] >= 1:
                                amount = produto.get("amount")
                                amount += 1
                                produto["amount"] = amount
                                cart.remove(produto)
                                cart.append(produto)
                                print(f"\033[0;32mMais um(a) {name} adicionado ao carrinho!\033[m")
                                added = True
                                break
                        elif tamanho == contador:
                            cart.append(produto)
                            print(f"\033[0;32m{name} adicionado ao carrinho!\033[m")
                            added = True
                            break
                        contador += 1
            elif added == False and ids == 157:
                sleep(1)
                print(f"\033[0;31mProduto não encontrado!\033[m")
        sleep(0.5)
        while True:
            escolha = str(input("\033[0;33mDeseja adicionar mais itens ao carrinho? (sim/nao) \033[m"))
            if escolha in "nao":
                return_to_the_question = False
                break
            elif escolha in "sim":
                break
            else:
                sleep(1)
                print(f"\033[0;31mDigite apenas: sim/nao\033[m")
# REMOVER UM PRODUTO
def remover_produto():
    print("="*57)
    sleep(0.2)
    print("\033[0;32mSegue abaixo os itens contidos no seu carrinho:\033[m")
    sleep(0.5)
    print("\033[0;33mNome                    Preço          Id      Quantidade\033[m")
    for item in cart:
        sleep(0.5)
        print(f"{item['name']:<23}", f"{item['price']:<12.2f}", "(", f"{item['id']}", ")", f"{item['amount']:>9}")
    sleep(0.5)
    # TIRAR VARIÁVEL
    var = True
    if len(cart) == 0:
        sleep(1)
        print(f"\033[0;31mVocê não tem produtos em seu carrinho!\033[m")
    else:
        while var == True:
            try:
                sleep(1)
                id = int(input("\033[0;33mDigite o ID do item que você deseja remover do carrinho? \033[m"))
                sleep(1)
                contador = 1
                for item in cart:
                    tamanho = len(cart)
                    if id == item["id"]:
                        if item["amount"] == 1:
                            cart.remove(item)
                            print(f"\033[0;32m{item['name']} removido do carrinho!\033[m")
                            var = False
                            break
                        else:
                            amount = item["amount"] - 1
                            item["amount"] = amount
                            cart.remove(item)
                            cart.append(item)
                            print(f"\033[0;32mUm(a) dos(as) {item['name']} foi removido do carrinho!\033[m")
                            var = False
                            break
                    elif tamanho == contador:
                        sleep(1)
                        print(f"\033[0;31mProduto não encontrado!\033[m")
                    contador += 1
            except ValueError:
                sleep(1)
                print(f"\033[0;31mDigite um número!\033[m")
    
# CONSULTAR VALOR DO CARRINHO
def consultar_carrinho(pago, valor_pago):
    soma = 0
    print("="*57)
    sleep(0.2)
    print("\033[0;33mSegue abaixo o valor total do seu carrinho:\033[m")
    sleep(1)
    if len(cart) != 0:
        for produto_no_carrinho in cart:
            quantidade = produto_no_carrinho["amount"]
            if quantidade > 1:
                soma += produto_no_carrinho["price"] * quantidade
            else:
                soma += produto_no_carrinho["price"]
    else:
        print(f"\033[0;32mA soma do seu carrinho deu R$0.00!\033[m")
        return pago, valor_pago
    print(f"\033[0;32mA soma do seu carrinho deu R${soma:.2f}!\033[m")
    sleep(1)
    if pago == True:
        if soma != valor_pago:
            print("\033[0;33mVocê tem produtos que não foram pagos! \033[m")
            soma -= valor_pago
            sleep(1)
            print(f"\033[0;33mA diferença é de R${soma:.2f}! \033[m")
            pago = False
    while True:
        if pago == False:
            sleep(1)
            escolha = str(input("\033[0;33mVocê deseja pagar a sua conta? (sim/nao) \033[m"))
            if escolha in "nao":
                break
            elif escolha in "sim":
                sleep(0.2)
                print("="*57)
                sleep(0.2)
                print("1 - Pagar no dinheiro")
                sleep(0.2)
                print("2 - Pagar no débito")
                sleep(0.2)
                print("3 - Pagar no crédito")
                sleep(0.2)
                opcao = int(input("\033[0;33mComo você deseja pagar a sua conta? \033[m"))
                sleep(1)
                if opcao == 1:
                    print(f"\033[0;32mVocê pagou R${soma:.2f} no dinheiro à vista!\033[m")
                    pago = True
                    valor_pago += soma
                    break
                elif opcao == 2:
                    print(f"\033[0;32mVocê pagou R${soma:.2f} no débito!\033[m")
                    pago = True
                    valor_pago += soma
                    break
                elif opcao == 3:
                    parcelas = int(input("\033[0;33mEm quantas parcelas você deseja pagar a sua conta? \033[m"))
                    sleep(1)
                    parcelado = soma / parcelas
                    print(f"\033[0;32mVocê irá pagar {parcelas}x de R${parcelado:.2f} no crédito!\033[m")
                    pago = True
                    valor_pago += soma
                    break
                else:
                    print(f"\033[0;31mDigite uma opção válida!\033[m")
            else:
                print(f"\033[0;31mDigite apenas: sim/nao\033[m")
        else:
            sleep(1)
            print(f"\033[0;32mA sua conta de R${soma:.2f} já foi paga!\033[m")
            break
    return pago, valor_pago