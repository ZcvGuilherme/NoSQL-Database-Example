from bson import ObjectId
from controller import *
from models import StatusLivro
import os
from time import sleep
def limpar_tela():
    sleep(1.5)
    os.system("cls" if os.name == "nt" else 'clear')

def exibir_menu():
    print("\n=== GERENCIADOR DE BIBLIOTECA ===")
    print("1. Inserir livro")
    print("2. Listar todos os livros")
    print("3. Listar livros por status")
    print("4. Emprestar livro")
    print("5. Devolver livro")
    print("6. Buscar por filtros")
    print("7. Ver histórico de um livro")
    print("8. Atualizar informações de um livro")
    print("9. Sair")

def escolher_status():
    print("Escolha o status:")
    for s in StatusLivro:
        print(f"- {s.value}")
    return input("Status: ").strip().lower()


while True:
    exibir_menu()
    opcao = input("Opção: ").strip()

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))
        inserir_livro(titulo, autor, ano)
        print("Livro inserido com sucesso.")
        limpar_tela()

    elif opcao == "2":
        livros = listar_livros()
        for livro in livros:
            print(f"{livro['_id']} | {livro['titulo']} | {livro['status']}")

    elif opcao == "3":
        status = escolher_status()
        livros = listar_livros(status)
        for livro in livros:
            print(f"{livro['_id']} | {livro['titulo']} | {livro['status']}")

    elif opcao == "4":
        id_livro = input("ID do livro: ").strip()
        if emprestar_livro(ObjectId(id_livro)):
            print("Livro emprestado com sucesso.")
        else:
            print("Livro não está disponível para empréstimo.")
        limpar_tela()

    elif opcao == "5":
        id_livro = input("ID do livro: ").strip()
        devolver_livro(ObjectId(id_livro))
        print("Livro devolvido com sucesso.")
        limpar_tela()
    elif opcao == "6":
        filtros = {}
        autor = input("Filtrar por autor (enter para ignorar): ").strip()
        ano = input("Filtrar por ano (enter para ignorar): ").strip()
        status = input("Filtrar por status (enter para ignorar): ").strip().lower()

        if autor:
            filtros["autor"] = autor
        if ano:
            filtros["ano"] = int(ano)
        if status:
            filtros["status"] = status

        resultados = buscar_por_filtros(filtros)
        for livro in resultados:
            print(f"{livro['_id']} | {livro['titulo']} | {livro['autor']} | {livro['ano']} | {livro['status']}")
    elif opcao == "7":
        id_livro = input("ID do livro: ").strip()
        historico = ver_historico(ObjectId(id_livro))
        for entrada in historico:
            print(f"{entrada['acao']} - {entrada['data']}")
    elif opcao == "8":
        id_livro = input("ID do livro: ").strip()
        novos_dados = {}
        titulo = input("Novo título (enter para manter): ").strip()
        autor = input("Novo autor (enter para manter): ").strip()
        ano = input("Novo ano (enter para manter): ").strip()

        if titulo:
            novos_dados["titulo"] = titulo
        if autor:
            novos_dados["autor"] = autor
        if ano:
            novos_dados["ano"] = int(ano)

        atualizar_info(ObjectId(id_livro), novos_dados)
        print("Informações atualizadas.")
        limpar_tela()
    elif opcao == "9":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
        limpar_tela()
