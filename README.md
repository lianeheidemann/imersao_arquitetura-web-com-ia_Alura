# Alura Álbum - Copa do Mundo Tech

![HTML5](https://img.shields.io/badge/HTML5-E34C26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


Este projeto é um **álbum de figurinhas digital e interativo** temático de tecnologia, contendo grandes pioneiros da computação e inteligência artificial, além de instrutores e personalidades da Alura. Ele foi desenvolvido como parte da **Imersão de Arquitetura Web com IA da Alura**.

O projeto simula a experiência física de folhear um álbum de figurinhas de papel diretamente no navegador, completo com animações realistas de transição e efeitos sonoros dinâmicos.

---

## Objetivo do Projeto

O objetivo foi construir uma aplicação frontend interativa integrada com recursos modernos do navegador e uma API backend (FastAPI) para o carregamento dinâmico das figurinhas. A aplicação serve de base para o aprendizado de arquitetura web, manipulação do DOM, estilização avançada, síntese de áudio no navegador e integrações de APIs.

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
│   ├── .venv/           # Ambiente Virtual 
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

Em outro terminal, ainda na pasta "frontend", execute:

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

Com o backend em execução, a documentação interativa pode ser acessada 

## Configuração

Por padrão, o frontend consulta a API em `http://localhost:8000`. Caso o
backend seja executado em outro endereço, altere a constante `API_BASE_URL` no
arquivo `frontend/app.js`.
