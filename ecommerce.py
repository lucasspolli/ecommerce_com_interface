from time import sleep
from funcoes_ecommerce import *

inicio()
sleep(1)
print("\033[0;33mSeja bem vindo(a) ao maior e-commerce da América Latina!\033[m")
sleep(1.5)
key = True
pago = False
valor_pago = 0
while key == True:
    sleep(0.5)
    opcao = menu()
    if opcao == 1:
        sleep(1)
        adicionar_produto()
    elif opcao == 2:
        sleep(1)
        remover_produto()
    elif opcao == 3:
        sleep(1)
        pago, valor_pago = consultar_carrinho(pago, valor_pago)
    elif opcao == 4:
        sleep(1)
        break
    else:
        sleep(1)
        print(f"\033[0;31mOpção inválida!\033[m")
sleep(1)
print("="*57)
sleep(0.5)
print("\033[0;33mObrigado por usar o nosso e-commerce! Volte sempre!\033[m")