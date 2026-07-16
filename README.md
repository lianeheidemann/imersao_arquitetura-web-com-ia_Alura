# Alura Album - Copa do Mundo Tech

Este projeto é um **álbum de figurinhas digital e interativo** temático de tecnologia, contendo grandes pioneiros da computação e inteligência artificial, além de instrutores e personalidades da Alura. Ele foi desenvolvido como parte da **Imersão de Arquitetura Web com IA da Alura**.

O projeto simula a experiência física de folhear um álbum de figurinhas de papel diretamente no navegador, completo com animações realistas de transição e efeitos sonoros dinâmicos.

---

## 🚀 Objetivo do Projeto

O objetivo principal é construir uma aplicação frontend interativa integrada com recursos modernos do navegador e, futuramente, consumindo uma API backend (FastAPI) para o carregamento dinâmico das figurinhas. A aplicação serve de base para o aprendizado de arquitetura web, manipulação do DOM, estilização avançada, síntese de áudio no navegador e integrações de APIs.

---

## 📂 Estrutura e Funcionalidade dos Arquivos

O projeto está estruturado da seguinte forma:

```text
├── code/
│   ├── assets/
│   │   └── figurinhas/     # Imagens das figurinhas (.jpg, .png, etc.)
│   ├── index.html          # Estrutura HTML do álbum
│   ├── style.css           # Estilização visual e animações
│   └── app.js              # Comportamento interativo e integração com a API
└── Material das aulas/
    └── Aula 1 - Prompts.txt # Exercícios e prompts da aula 1
```

### Detalhamento dos Arquivos

1. **[index.html](file:///c:/Users/Lily/Documents/GitHub/Alura_ArquiteturaWebComIA/code/index.html)**
   * **Função**: Define a estrutura semântica do álbum de figurinhas.
   * **Conteúdo**: Contém a estrutura da capa e as páginas internas categorizadas (como pioneiros da IA, Python, Bancos de Dados e figuras da Alura). Cada página possui uma grade de *slots* (espaços) numerados onde as figurinhas serão inseridas. Também inclui os botões de navegação lateral e controle de áudio.

2. **[style.css](file:///c:/Users/Lily/Documents/GitHub/Alura_ArquiteturaWebComIA/code/style.css)**
   * **Função**: Gerencia todo o design visual, cores e layout responsivo.
   * **Conteúdo**: Utiliza variáveis CSS (`:root`) para definir uma paleta de cores moderna inspirada no espaço/tecnologia. Inclui o layout tridimensional em grade para os slots de figurinhas, sombreamento das páginas simulando a lombada de um livro, cursor personalizado para ações de arrastar (`grab`/`grabbing`) e efeitos visuais avançados como o efeito *glitch* na capa.

3. **[app.js](file:///c:/Users/Lily/Documents/GitHub/Alura_ArquiteturaWebComIA/code/app.js)**
   * **Função**: Controla a lógica e a interatividade da aplicação.
   * **Conteúdo**:
     * **Virada de Página**: Inicializa e configura a biblioteca `St.PageFlip` para permitir a paginação do álbum (via mouse, gestos de toque ou setas do teclado).
     * **Efeito Sonoro**: Utiliza a *Web Audio API* para sintetizar via código um som realista de papel virando (ruído branco com filtros dinâmicos e controle de volume).
     * **Carregamento Dinâmico**: Realiza uma requisição assíncrona (`fetch`) para a API backend no endereço `http://localhost:8000/figurinhas` para obter as informações das figurinhas e inseri-las dinamicamente nos respectivos *slots* do HTML.

4. **[assets/figurinhas/](file:///c:/Users/Lily/Documents/GitHub/Alura_ArquiteturaWebComIA/code/assets/figurinhas)**
   * **Função**: Armazena as imagens estáticas das figurinhas que correspondem a cada um dos pioneiros e instrutores (ex.: Alan Turing, Linus Torvalds, Paulo Silveira, etc.).

5. **[Material das aulas/Aula 1 - Prompts.txt](file:///c:/Users/Lily/Documents/GitHub/Alura_ArquiteturaWebComIA/Material%20das%20aulas/Aula%201%20-%20Prompts.txt)**
   * **Função**: Arquivo de texto que serve de guia e apoio, contendo a lista de exercícios e roteiros propostos para as práticas de Inteligência Artificial da Aula 1.

---

## 🛠️ Tecnologias Utilizadas

* **HTML5**: Estruturação semântica.
* **CSS3**: Layouts com Flexbox/Grid, variáveis de ambiente, efeitos de gradiente e animações de transição.
* **JavaScript (ES6+)**: Manipulação de DOM, requisições assíncronas (`fetch`) e lógica de navegação.
* **St.PageFlip**: Biblioteca externa para a simulação física do livro.
* **Web Audio API**: Geração e síntese de áudio nativa no navegador para simulação acústica realista de papel.

---

## 🚦 Como Executar o Projeto

1. **Frontend**:
   * Basta abrir o arquivo `code/index.html` diretamente no seu navegador, ou utilizar uma extensão como o *Live Server* no VS Code para servir os arquivos localmente.
2. **Backend (Opcional - Fase Posterior)**:
   * Conforme indicado no código, as figurinhas dinâmicas são carregadas de uma API local. Para executá-la (quando disponível), execute os seguintes comandos no terminal:
     ```bash
     cd backend/dia-3
     uvicorn main:app --reload
     ```
