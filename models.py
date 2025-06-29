from enum import Enum

class StatusLivro(str, Enum):
    DISPONIVEL = "disponível"
    EMPRESTADO = "emprestado"
    RESERVADO = "reservado"
