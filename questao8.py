import json
import os
from datetime import datetime


ARQUIVO = "shows.json"


def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    return []


def salvar(shows):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(shows, arquivo, ensure_ascii=False, indent=2)


def ordenar_shows(shows):
    return sorted(
        shows,
        key=lambda show: datetime.strptime(show["data"], "%d/%m/%Y")
    )


def listar(shows):
    if len(shows) == 0:
        print("Não há shows cadastrados.")
        return

    organizados = ordenar_shows(shows)

    for i, show in enumerate(organizados):
        situacao = ""

        if show["ingressos"] == 0:
            situacao = " ESGOTADO"

        print(
            f'{i + 1}. {show["data"]} '
            f'{show["artista"]:25} '
            f'{show["cidade"]:18} '
            f'R$ {show["preco"]:8.2f} '
            f'{show["ingressos"]} ingressos{situacao}'
        )


def cadastrar(shows):
    artista = input("Artista/banda: ")
    cidade = input("Cidade: ")

    while True:
        data = input("Data (dd/mm/aaaa): ")

        try:
            datetime.strptime(data, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Digite no formato dd/mm/aaaa.")

    while True:
        try:
            preco = float(input("Preço do ingresso: R$ ").replace(",", "."))
            if preco > 0:
                break
            print("O preço deve ser maior que zero.")
        except ValueError:
            print("Digite um preço válido.")

    while True:
        try:
            ingressos = int(input("Ingressos disponíveis: "))
            if ingressos >= 0:
                break
            print("Digite zero ou um número positivo.")
        except ValueError:
            print("Digite um número inteiro.")

    show = {
        "artista": artista,
        "cidade": cidade,
        "data": data,
        "preco": preco,
        "ingressos": ingressos
    }

    shows.append(show)
    salvar(shows)

    print("Show cadastrado e agenda salva.")


def shows_cidade(shows):
    cidade = input("Cidade: ")
    encontrados = []

    for show in shows:
        if cidade.lower() in show["cidade"].lower():
            encontrados.append(show)

    if encontrados:
        listar(encontrados)
    else:
        print("Nenhum show encontrado nessa cidade.")


def vender(shows):
    organizados = ordenar_shows(shows)

    if not organizados:
        print("Não há shows cadastrados.")
        return

    listar(shows)

    try:
        numero = int(input("Número do show: "))

        if numero < 1 or numero > len(organizados):
            print("Número de show inválido.")
            return

        show = organizados[numero - 1]

        quantidade = int(input("Quantos ingressos? "))

        if quantidade <= 0:
            print("Digite uma quantidade maior que zero.")
        elif quantidade > show["ingressos"]:
            print(f"Só restam {show['ingressos']} ingressos.")
        else:
            show["ingressos"] -= quantidade

            valor = quantidade * show["preco"]

            salvar(shows)

            print(
                f"Venda: {quantidade} x R$ {show['preco']:.2f} "
                f"= R$ {valor:.2f}"
            )

    except ValueError:
        print("Digite um número válido.")


def remover(shows):
    organizados = ordenar_shows(shows)

    if not organizados:
        print("Não há shows cadastrados.")
        return

    listar(shows)

    try:
        numero = int(input("Número do show: "))

        if numero < 1 or numero > len(organizados):
            print("Número inválido.")
            return

        show = organizados[numero - 1]

        shows.remove(show)
        salvar(shows)

        print(f"Show de {show['artista']} removido.")

    except ValueError:
        print("Digite um número válido.")


shows = carregar()

print(f"Agenda carregada: {len(shows)} shows.")

while True:
    print("\n===== AGENDA DE SHOWS =====")
    print("1 - Listar shows")
    print("2 - Cadastrar show")
    print("3 - Shows em uma cidade")
    print("4 - Vender ingressos")
    print("5 - Remover show")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        listar(shows)

    elif opcao == "2":
        cadastrar(shows)

    elif opcao == "3":
        shows_cidade(shows)

    elif opcao == "4":
        vender(shows)

    elif opcao == "5":
        remover(shows)

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")