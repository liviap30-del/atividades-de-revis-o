def subtotal_item(preco, quantidade=1):
    return preco * quantidade


def aplicar_cupom(total, cupom):
    cupom = cupom.strip().upper()

    descontos = {
        "PROMO10": 10,
        "VOLTAASAULAS": 15,
        "BLACK25": 25
    }

    percentual = descontos.get(cupom, 0)

    novo_total = total - (total * percentual / 100)

    return novo_total, percentual


def calcular_frete(total, gratis_acima=200.0, valor=25.0):
    if total >= gratis_acima:
        return 0.0

    return valor


def valor_parcela(total, parcelas=1):
    if parcelas <= 6:
        return total / parcelas

    return total * (1 + 0.02 * parcelas) / parcelas


print("=== LOJA VIRTUAL ===")

subtotal = 0

while True:
    produto = input("\nProduto (Enter para fechar o carrinho): ")

    if produto == "":
        break

    while True:
        try:
            preco = float(input("Preço: R$ ").replace(",", "."))

            if preco > 0:
                break
            else:
                print("Digite um valor maior que zero.")

        except ValueError:
            print("Digite um preço válido.")

    while True:
        try:
            quantidade = int(input("Quantidade: "))

            if quantidade > 0:
                break
            else:
                print("Digite uma quantidade maior que zero.")

        except ValueError:
            print("Digite um número inteiro.")

    valor = subtotal_item(preco, quantidade)

    subtotal += valor

    print(f"{quantidade} x {produto} = R$ {valor:.2f}")
    print(f"Carrinho: R$ {subtotal:.2f}")

cupom = input("\nCupom de desconto (Enter se não tiver): ")

novo_total, percentual = aplicar_cupom(subtotal, cupom)

if cupom.strip() != "" and percentual == 0:
    print("Cupom inválido.")

desconto = subtotal - novo_total

frete = calcular_frete(novo_total)

while True:
    try:
        parcelas = int(input("Em quantas parcelas (1 a 12)? "))

        if 1 <= parcelas <= 12:
            break
        else:
            print("Digite um número entre 1 e 12.")

    except ValueError:
        print("Digite um número inteiro.")

total = novo_total + frete

parcela = valor_parcela(total, parcelas)

print("\n=== NOTA ===")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: {percentual}% (R$ {desconto:.2f})")
print(f"Frete: R$ {frete:.2f}")
print(f"Total: R$ {total:.2f}")
print(f"Pagamento: {parcelas} x R$ {parcela:.2f}")