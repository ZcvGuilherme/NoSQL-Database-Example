# 📚 Gerenciador de Biblioteca — Python + MongoDB

Projeto desenvolvido durante meu período de estudos no IFPI, com foco em aplicar os conceitos de **banco de dados NoSQL (MongoDB)** e **estrutura MVC em Python**.

---

## 🚀 Funcionalidades

Este sistema permite o gerenciamento completo de uma biblioteca com os seguintes recursos:

- ✅ Inserção de livros com status inicial "disponível"
- 📋 Listagem geral e por status (ex: apenas "emprestados")
- 🔄 Empréstimo e devolução de livros (com registro de histórico)
- 🔍 Busca avançada por múltiplos filtros (autor, ano e status)
- 🕓 Visualização do histórico de alterações de cada livro
- ✏️ Atualização das informações do livro (exceto status e histórico)

---

## 🧱 Tecnologias Utilizadas

- 🐍 **Python 3.x**
- 🍃 **MongoDB**
- 🧰 **Pymongo** (Driver oficial do MongoDB para Python)
- 📐 Estrutura **MVC** (Model - View - Controller)

---
## ▶️ Como Executar

1. Instale o MongoDB e certifique-se de que está rodando localmente (`mongodb://localhost:27017/`)
2. Instale o driver `pymongo`:

```bash
pip install pymongo
```

📌 Observações
- O sistema usa ObjectId como identificador único dos livros.

- O histórico de cada livro é armazenado como uma lista de ações com data/hora.

- A busca por autor e status é case-insensitive para facilitar o uso.

🧑‍💻 Autor
**Guilherme Sousa**
Estudante do Instituto Federal do Piauí (IFPI)
