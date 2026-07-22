# Alura Álbum — Copa do Mundo Tech

![HTML5](https://img.shields.io/badge/HTML5-E34C26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Álbum digital e interativo com temática de tecnologia, reunindo pioneiros da computação e da inteligência artificial, além de instrutores e personalidades da Alura.

O projeto foi desenvolvido durante a **Imersão Arquitetura Web com IA, da Alura**, com foco na integração entre frontend e backend.

---

## Objetivo do projeto

Aplicar conceitos de arquitetura web por meio de uma interface interativa conectada a uma API desenvolvida com Python e FastAPI.

O backend disponibiliza as imagens das figurinhas por meio de uma API REST, enquanto o frontend consome esses dados e renderiza o conteúdo dinamicamente na página.

---

## Tecnologias e conceitos aplicados

- HTML5
- CSS3
- JavaScript
- Python
- FastAPI
- API REST
- Manipulação do DOM
- Requisições HTTP
- Ambiente virtual com `venv`
- Integração entre frontend e backend
- Síntese de voz com recursos nativos do navegador

---

## Interface

![Interface](assets/gif/interface.gif)

---

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
│   ├── .venv/           # ambiente Virtual
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

Abra a pasta "backend" como raiz do projeto, crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
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

Em outro terminal, ainda na pasta "frontend", execute:

```bash
python -m http.server 5500 --directory frontend
```

Acesse `http://localhost:5500` no navegador. Mantenha os dois servidores em
execução para que as figurinhas sejam carregadas.

> Abrir o `index.html` diretamente permite visualizar o álbum, mas um servidor
> local é recomendado para evitar restrições do navegador.

<details>
    <summary>Se o ambiente virtual foi já criado anteriormente</summary>

<br>Para visualizar o álbum, execute o backend e o frontend em dois terminais.

No primeiro terminal, dentro de `backend`:

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

No segundo terminal:

```powershell
cd ..\frontend
..\backend\.venv\Scripts\python.exe -m http.server 5500
```

Depois, abra no navegador:

- Álbum: http://localhost:5500
- Documentação da API: http://localhost:8000/docs
- Lista de figurinhas: http://localhost:8000/figurinhas

Mantenha os dois terminais abertos. O frontend está configurado para buscar as imagens na API em `localhost:8000`.

---

</details>

## API

| Método | Rota                      | Descrição                         |
| ------ | ------------------------- | --------------------------------- |
| `GET`  | `/figurinhas`             | Lista as figurinhas disponíveis   |
| `GET`  | `/figurinhas/{id}/imagem` | Retorna a imagem de uma figurinha |

Com o backend em execução, a documentação interativa pode ser acessada em
`http://localhost:8000/docs`.

## Configuração

Por padrão, o frontend consulta a API em `http://localhost:8000`. Caso o
backend seja executado em outro endereço, altere a constante `API_BASE_URL` no
arquivo `frontend/app.js`.
