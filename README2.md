# Alura Album - Copa do Mundo Tech

Um **álbum de figurinhas digital e interativo** que celebra os pioneiros da computação, inteligência artificial e personalidades da Alura, com animações realistas e efeitos sonoros.

---

## 🎯 Objetivo

Desenvolver uma aplicação frontend interativa que simule a experiência clássica de folhear um álbum de papel, integrando tecnologias modernas do navegador e consumindo dados de uma API backend (FastAPI).

---

## 🛠️ Stack Tecnológico

| Tecnologia | Uso |
|-----------|-----|
| **HTML5** | Estrutura semântica |
| **CSS3** | Layout responsivo (Grid/Flexbox), animações e gradientes |
| **JavaScript (ES6+)** | Interatividade, requisições assíncronas |
| **St.PageFlip** | Simulação física de virada de páginas |
| **Web Audio API** | Síntese de áudio realista |

---

## 📂 Estrutura do Projeto

```
code/
├── index.html              # Estrutura e layout do álbum
├── style.css               # Design visual e animações
├── app.js                  # Lógica de interatividade
└── assets/figurinhas/      # Imagens das figurinhas
```

---

## ⚡ Funcionalidades Principais

- ✅ **Virada de Páginas**: Navegação via mouse, toque ou teclado
- ✅ **Efeitos Sonoros**: Som realista de papel virando (síntese por código)
- ✅ **Carregamento Dinâmico**: Integração com API backend para dados das figurinhas
- ✅ **Design Responsivo**: Tema inspirado em tecnologia com paleta moderna

---

## 🚀 Como Usar

### Frontend
```bash
# Abra diretamente no navegador
code/index.html

# Ou use Live Server (VS Code)
```

### Backend (opcional)
```bash
cd backend/dia-3
uvicorn main:app --reload
# API disponível em: http://localhost:8000/figurinhas
```

---

## 📊 Composição do Projeto

- CSS: 38.4%
- HTML: 35.3%
- JavaScript: 24.1%
- Python: 2.2%

---

## 📚 Recursos Adicionais

- Material das aulas disponível em `Material das aulas/`
- Prompts e exercícios inclusos na documentação

---

## 📝 Licença

Projeto desenvolvido como parte do curso **Arquitetura Web com IA** da Alura.
