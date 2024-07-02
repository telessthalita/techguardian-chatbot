from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a string de conexão do arquivo .env
mongo_uri = os.getenv('MONGO_URI')

# Conecta-se ao MongoDB
client = MongoClient(mongo_uri)

# Especifique o banco de dados que deseja acessar
db = client.get_database('chat_bot')

@app.route('/')
def home():
    return 'Conexão com MongoDB estabelecida!'

if __name__ == '__main__':
    app.run(debug=True)
