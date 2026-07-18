# Prompts - Aula 2

1. Crie um ambiente virtual em Python usando a venv e faça a ativação

<!-- O Uvicorn é um servidor web ASGI (Asynchronous Server Gateway Interface) ultrarrápido para Python. Ele é o motor padrão de frameworks assíncronos modernos como o FastAPI e o Starlette, projetado para suportar conexões persistentes, como WebSockets e HTTP/1.1.Ele é frequentemente utilizado para iniciar aplicativos e APIs localmente ou em ambientes de produção

Para ativá-lo no Terminal:
.\.venv\Scripts\Activate.ps1

Rodando direto usando a pasta do ambiente virtual (Recomendado no Windows):
.venv\Scripts\uvicorn main:app --reload

Ver no Chrome a aplicação: http://127.0.0.1:8000
Ver a Documentação: http://127.0.0.1:8000/doc -->

2.  No Terminal: pip install fastapi

3.  Instale o uvicorn na venv deste projeto

4.  Você vai criar o primeiro servidor de uma API de álbum de figurinhas.

    Crie um arquivo main.py com um servidor FastAPI que tenha apenas 1 endpoint:
    1. GET "/" → retorna o JSON {"mensagem": "Olá, mundo! 🌍"}
       (use uma função chamada hello_world)

    Requisitos:
    - Use apenas Python com FastAPI (import: from fastapi import FastAPI)
    - Crie a aplicação com app = FastAPI()
    - Adicione comentários em português explicando cada parte
    - Não adicione nenhum outro endpoint

5.  No mesmo arquivo main.py, adicione um segundo endpoint, mantendo o endpoint "/" que já existe: 2. GET "/figurinhas" → retorna uma lista com 2 figurinhas de exemplo
    (use uma função chamada listar_figurinhas)
    Cada figurinha é um objeto com os campos:

              * id (número inteiro)
              * nome (texto)
              * categoria (texto)

        Use estas duas figurinhas:
        _ {id: 1, nome: "Alan Turing", categoria: "IA"}
        _ {id: 2, nome: "John McCarthy", categoria: "IA"}

    Requisitos:
    - Mantenha tudo que já existe no arquivo
    - Adicione comentários em português
    - Não adicione nenhum endpoint além desses dois
    
