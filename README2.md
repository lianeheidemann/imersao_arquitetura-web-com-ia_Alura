## Tecnologias

| Camada   | Tecnologias                                         |
| -------- | --------------------------------------------------- |
| Frontend | HTML5, CSS3 e JavaScript                            |
| Animação | [St.PageFlip](https://nodlik.github.io/StPageFlip/) |
| Áudio    | Web Audio API                                       |
| Backend  | Python, FastAPI e Uvicorn                           |

O frontend não utiliza gerenciador de pacotes. A biblioteca de virada de
página e as fontes são carregadas por CDN.

## Estrutura do projeto

```text
├── backend/
│   ├── figurinhas/      # imagens servidas pela API
│   └── main.py          # aplicação FastAPI
├── frontend/
│   ├── app.js           # integração com a API e interações
│   ├── index.html       # estrutura do álbum
│   └── style.css        # estilos e responsividade
└── README.md
```

## Como executar

### Pré-requisitos

- Python 3.10 ou superior;
- acesso à internet para carregar o St.PageFlip e as fontes do Google.

### 1. Prepare o backend

Na raiz do projeto, crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install fastapi uvicorn
```

Inicie a API:

```bash
uvicorn backend.main:app --reload
```

A API ficará disponível em `http://localhost:8000`.

### 2. Inicie o frontend

Em outro terminal, ainda na raiz do projeto, execute:

```bash
python -m http.server 5500 --directory frontend
```

Acesse `http://localhost:5500` no navegador. Mantenha os dois servidores em
execução para que as figurinhas sejam carregadas.

> Abrir o `index.html` diretamente permite visualizar o álbum, mas um servidor
> local é recomendado para evitar restrições do navegador.

## API

| Método | Rota                      | Descrição                         |
| ------ | ------------------------- | --------------------------------- |
| `GET`  | `/figurinhas`             | Lista as figurinhas disponíveis   |
| `GET`  | `/figurinhas/{id}/imagem` | Retorna a imagem de uma figurinha |

Com o backend em execução, a documentação interativa pode ser acessada em

## Configuração

Por padrão, o frontend consulta a API em `http://localhost:8000`. Caso o
backend seja executado em outro endereço, altere a constante `API_BASE_URL` no
arquivo `frontend/app.js`.
