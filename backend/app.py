from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_cors import CORS
from config.config import Config  # Ajuste no caminho de importação

# Inicializar a instância do SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Criar uma instância do Flask
    app = Flask(__name__, template_folder='templates')
    
    # Carregar as configurações da classe Config
    app.config.from_object(Config)
    
    # Desativar o rastreamento de modificações do SQLAlchemy para economizar recursos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar a instância do SQLAlchemy com a aplicação Flask
    db.init_app(app)
    
    # Adicionar suporte a CORS (Cross-Origin Resource Sharing)
    CORS(app)

    # Importar e registrar o blueprint de rotas
    from routes import routes
    app.register_blueprint(routes)

    # Testar a conexão com o banco de dados
    try:
        with app.app_context():
            with db.engine.connect() as connection:
                connection.execute(text('SELECT 1'))
        print("Conexão com o banco de dados bem-sucedida!")
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

    return app

if __name__ == '__main__':
    # Criar a aplicação Flask
    app = create_app()
    
    # Criar todas as tabelas no banco de dados
    with app.app_context():
        db.create_all()
    
    # Executar a aplicação Flask em modo de depuração
    app.run(debug=True)