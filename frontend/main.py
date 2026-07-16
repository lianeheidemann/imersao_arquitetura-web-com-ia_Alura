# Importa a classe FastAPI do framework fastapi para criar o servidor
from fastapi import FastAPI

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Define uma rota para requisições do tipo GET no caminho raiz "/"
@app.get("/")
def hello_world():
    # Retorna um dicionário que o FastAPI converterá automaticamente em formato JSON
    return {"mensagem": "Olá, mundo! 🌍"}
