# Alura Album - Copa do Mundo Tech

Álbum de figurinhas digital e interativo temático de tecnologia. Projeto educacional que simula a experiência física de folhear um álbum de papel, completo com animações realistas e integração com API backend.

## 🎯 Objetivo

Desenvolver uma aplicação frontend interativa que demonstra arquitetura web moderna com recursos de navegador avançados, consumindo dados de uma API backend (FastAPI) para carregamento dinâmico de figurinhas.

## 📂 Estrutura do Projeto

```
code/
├── assets/figurinhas/     # Imagens das figurinhas
├── index.html             # Estrutura HTML
├── style.css              # Estilos e animações
└── app.js                 # Lógica interativa
```

## 🛠️ Tecnologias

| Tecnologia | Uso |
|-----------|-----|
| **HTML5** | Estruturação semântica |
| **CSS3** | Layout (Flexbox/Grid), animações, gradientes |
| **JavaScript (ES6+)** | Interatividade, requisições assíncronas |
| **St.PageFlip** | Simulação de virada de páginas |
| **Web Audio API** | Síntese de som de papel virando |
| **FastAPI** | Backend (configuração futura) |

## 🚀 Como Usar

### Frontend

```bash
# Abra diretamente no navegador
code/index.html

# Ou use Live Server (VS Code)
```

### Backend (Opcional)

```bash
cd backend/dia-3
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000/figurinhas`

## 📋 Funcionalidades

- ✨ Interatividade com mouse, toque e teclado
- 🎵 Efeito sonoro realista de virada de página
- 📱 Layout responsivo
- 🔄 Carregamento dinâmico de figurinhas via API
- 🎨 Design moderno com paleta inspirada em tecnologia

## 📁 Repositório

- **Linguagens**: CSS (38.4%), HTML (35.3%), JavaScript (24.1%), Python (2.2%)
- **Privacidade**: Privado
- **Licença**: Sem licença especificada

---

**Desenvolvido como projeto educacional da Alura sobre Arquitetura Web com IA.**
