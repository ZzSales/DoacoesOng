# Sistema de Doações para ONG

Este projeto é um sistema de doações desenvolvido para facilitar a arrecadação de fundos para ONGs. O sistema é dividido em duas partes principais: o backend, que gerencia a lógica do servidor e a interação com o banco de dados, e o frontend, que fornece a interface do usuário.

## Estrutura do Projeto

```
donation-system
├── backend
│   ├── app.py          # Ponto de entrada da aplicação backend
│   ├── models.py       # Modelos de dados para doações e doadores
│   ├── routes.py       # Rotas da API para gerenciar doações
│   └── requirements.txt # Dependências do backend
├── frontend
│   ├── index.html      # Página principal da aplicação frontend
│   ├── app.js          # Lógica do frontend
│   └── styles.css      # Estilos CSS para a interface
├── database
│   └── schema.sql      # Script SQL para criar tabelas no banco de dados
├── config
│   └── config.py       # Configurações da aplicação
├── scripts
│   └── setup.sh        # Script de configuração do ambiente
└── README.md           # Documentação do projeto
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd donation-system
   ```

2. Configure o ambiente virtual e instale as dependências do backend:
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   pip install -r requirements.txt
   ```

3. Configure o banco de dados:
   - Edite o arquivo `config/config.py` com suas credenciais do PostgreSQL.
   - Execute o script SQL em `database/schema.sql` para criar as tabelas necessárias.

4. Inicie o servidor backend:
   ```
   python app.py
   ```

5. Abra o arquivo `frontend/index.html` em um navegador para acessar a aplicação.

## Uso

- O sistema permite que os usuários façam doações, registrando seus dados e a quantia doada.
- A interface do usuário é responsiva e fácil de usar, permitindo uma experiência fluida.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.