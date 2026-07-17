Para visualizar o álbum, execute o backend e o frontend em dois terminais.

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
