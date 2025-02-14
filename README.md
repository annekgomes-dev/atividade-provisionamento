# Passo a passo para executar a aplicação com Docker

## 1. Estrutura do projeto

```
project/
├── backend/
    |── app.py
    ├── Dockerfile
    ├── requirements.txt
├── .env
├── docker-compose.yml
```

## 2. Criar um arquivo `.env` para armazenar credenciais com segurança
Crie um arquivo `.env` na raiz do projeto e adicione:
```
POSTGRES_USER= xxxx
POSTGRES_PASSWORD= xxxx
POSTGRES_DB=mydatabase
```

## 3. Arquivo `docker-compose.yml`
```yaml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
    depends_on:
      - db
    volumes:
      - ./backend:/app

  db:
    image: postgres:latest
    restart: always
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```  

## 4. Arquivo `Dockerfile` para o backend
```dockerfile
# Use uma imagem oficial do Python
FROM python:3.9-alpine

# Defina o diretório de trabalho
WORKDIR /app

# Copie apenas os arquivos necessários para instalar as dependências
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos
COPY . .

# Exponha a porta 5000
EXPOSE 5000

# Comando para rodar o aplicativo
CMD ["python", "app.py"]
```

## 5. Código do backend em Python
```python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Aplicação Flask rodando com Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## 6. Arquivo `requirements.txt`
```
Flask
```

## 7. Comando para construir e rodar os contêineres

```sh
docker-compose up --build
```

## 8. Resultado no navegador
```
Aplicação Flask rodando com Docker!
```

## 9. Parar os contêineres

```sh
docker-compose down
```
