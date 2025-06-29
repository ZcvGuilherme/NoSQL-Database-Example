from db import livros
from models import StatusLivro
from datetime import datetime

def inserir_livro(titulo, autor, ano):
    novo = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "status": StatusLivro.DISPONIVEL.value,
        "historico": [{"acao": "inserido", "data": datetime.now()}]
    }
    livros.insert_one(novo)

def listar_livros(status=None):
    filtro = {"status": status} if status else {}
    return list(livros.find(filtro))

def emprestar_livro(id_livro):
    livro = livros.find_one({"_id": id_livro})
    if livro["status"] != StatusLivro.DISPONIVEL:
        return False
    livros.update_one(
        {"_id": id_livro},
        {"$set": {"status": StatusLivro.EMPRESTADO.value},
         "$push": {"historico": {"acao": "emprestado", "data": datetime.now()}}}
    )
    return True

def devolver_livro(id_livro):
    livros.update_one(
        {"_id": id_livro},
        {"$set": {"status": StatusLivro.DISPONIVEL.value},
         "$push": {"historico": {"acao": "devolvido", "data": datetime.now()}}}
    )

def atualizar_info(id_livro, novos_dados: dict):
    novos_dados.pop("status", None)
    novos_dados.pop("historico", None)
    livros.update_one({"_id": id_livro}, {"$set": novos_dados})
    
def buscar_por_filtros(filtros: dict):
    consulta = {}

    if "autor" in filtros:
        consulta["autor"] = {"$regex": filtros["autor"], "$options": "i"}

    if "status" in filtros:
        consulta["status"] = {"$regex": filtros["status"], "$options": "i"}

    if "ano" in filtros:
        consulta["ano"] = filtros["ano"]  # Comparação direta de número

    return list(livros.find(consulta))

def ver_historico(id_livro):
    livro = livros.find_one({"_id": id_livro})
    return livro.get("historico", [])
