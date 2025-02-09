import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    # Ativar ou desativar o modo de depuração com base na variável de ambiente DEBUG
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    
    # URL de conexão com o banco de dados, obtida da variável de ambiente DATABASE_URI
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql+psycopg2://postgres:crvg2004Gust%40@localhost:5432/postgres?client_encoding=utf8')
    
    # Desativar o rastreamento de modificações do SQLAlchemy para economizar recursos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Chave secreta para a aplicação Flask, obtida da variável de ambiente SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')