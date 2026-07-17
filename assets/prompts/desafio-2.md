Desafio 2: Buscar uma figurinha pelo id (com erro 404) 



No Dia 2, o main.py tem dois endpoints: GET / e GET /figurinhas (que devolve a lista das 2 figurinhas em JSON). Seu desafio é instruir a IA a adicionar um terceiro endpoint que busca uma única figurinha pelo seu id: 



GET /figurinhas/1 → devolve a figurinha do Alan Turing 



GET /figurinhas/2 → devolve a figurinha do John McCarthy 



GET /figurinhas/99 → devolve erro 404 (não encontrado), porque esse id não existe 



O segredo aqui é o parâmetro de rota dinâmico ({id}) e o status code 404 — conceitos que apareceram na aula do Dia 1. 



💡 Dica para solucionar 



Seu prompt precisa deixar claro que é para adicionar ao arquivo existente, mantendo os endpoints / e /figurinhas. Cole o conteúdo atual do main.py no prompt para dar contexto. 



Especifique o comportamento dos dois caminhos: quando o id existe (retorna a figurinha) e quando não existe (retorna 404). 



Mencione que, no FastAPI, o erro 404 se faz com HTTPException — ou simplesmente peça "retorne erro 404 se o id não existir" e deixe a IA escolher a forma. 

