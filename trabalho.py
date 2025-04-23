class ProdutoInvalidoError(Exception):
    def __init__(self, produto):
        super().__init__(f"O produto '{produto}' não está disponível.")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, total):
        super().__init__(f"Saldo insuficiente. Saldo disponível: {saldo:.2f}€, Total da compra: {total:.2f}€")


produtos_disponiveis = {
    "bola": 10.0,
    "teclado": 80.0,
    "sapatos": 50.0,
    
}

carrinho = {}
saldo = 300.0

def mostrar_produtos():
    print("\nProdutos disponíveis:")
    for nome, preco in produtos_disponiveis.items():
        print(f"{nome}: {preco:.2f}€")

def adicionar_ao_carrinho():
    try:
        produto = input("Introduza o nome do produto que deseja adicionar: ").lower()
        if produto not in produtos_disponiveis:
            raise ProdutoInvalidoError(produto)

        quantidade = int(input("Informe a quantidade: "))
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser um número positivo.")

        if produto in carrinho:
            carrinho[produto] += quantidade
        else:
            carrinho[produto] = quantidade
        

    except ProdutoInvalidoError as e:
        print(f"Erro: {e}")
    except ValueError:
        print("Erro: Quantidade inválida. Digite positivo.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def Carrinho():
    if not carrinho:
        print("O carrinho está vazio.")
        return

    print("\nCarrinho de Compras:")
    total = 0
    for produto, quantidade in carrinho.items():
        preco = produtos_disponiveis[produto]
        subtotal = preco * quantidade
        print(f"{produto} x{quantidade} -{subtotal:.2f}€")
        total += subtotal
    print(f"Total: {total:.2f}€")

def pagamento():
    global saldo
    if not carrinho:
        print("Erro: Carrinho vazio. Adiciona algum produto antes de pagar.")
        return

    total = sum(produtos_disponiveis[produtos] * quantidade for produtos, quantidade in carrinho.items())
    
    try:
        if total > saldo:
            raise SaldoInsuficienteError(saldo, total)
        else:
            saldo -= total
            print(f"Pagamento realizado com sucesso! Saldo restante: {saldo:.2f}€")
            carrinho.clear()

    except SaldoInsuficienteError as e:
        print(f"Erro: {e}")

def menu():
    while True:
        print("LOJA VIRTUAL")
        print("1. Mostrar produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Ver carrinho")
        print("4. Pagamento")
        print("5. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                mostrar_produtos()
            elif opcao == 2:
                adicionar_ao_carrinho()
            elif opcao == 3:
                Carrinho()
            elif opcao == 4:
                pagamento()
            elif opcao == 5:
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Erro: Insere um número válido.")

if __name__ == "__main__":
    menu()