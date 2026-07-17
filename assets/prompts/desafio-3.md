Desafio 3: Endpoint de contagem e estatística do álbum



No Dia 3, o main.py tem a lista figurinhas (hoje com 2 itens) e o endpoint GET /figurinhas que a devolve em JSON. Mas o álbum completo tem 25 slots para preencher.



Seu desafio é instruir a IA a adicionar um novo endpoint GET /figurinhas/total que não devolve a lista, e sim uma estatística calculada a partir dela:



{

&#x20; "total\_album": 25,

&#x20; "coladas": 2,

&#x20; "faltam": 23

}



O pulo do gato: o número de coladas e o de faltam devem ser calculados a partir da lista (não escritos "na mão"). Assim, quando alguém adicionar uma figurinha à lista, a estatística se atualiza sozinha.







💡 Dica para solucionar



No prompt, deixe claro que é para adicionar o endpoint, mantendo o GET /figurinhas que já existe. Cole a lista atual para dar contexto.



O total do álbum (25) é uma constante — diga isso. Já as coladas saem de len(figurinhas) e faltam é 25 - len(figurinhas).



Reforce que os valores devem ser calculados a partir da lista, e não valores fixos — é isso que torna o endpoint "vivo".



Peça para a IA usar uma função com nome claro (ex: estatisticas\_album).



Bora concluir esse último desafio?

