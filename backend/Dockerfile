# Use uma imagem oficial do Python
FROM python:3.9-alpine

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos para o contêiner
COPY . .

# Instale as dependências
RUN pip install -r requirements.txt

# Exponha a porta 5000
EXPOSE 5000

# Comando para rodar o aplicativo
CMD ["python", "app.py"]