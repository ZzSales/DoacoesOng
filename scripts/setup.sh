#!/bin/bash

# Atualiza o sistema
sudo apt update && sudo apt upgrade -y

# Instala o Python e pip
sudo apt install python3 python3-pip -y

# Instala o PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Cria um ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instala as dependências do backend
pip install -r ../backend/requirements.txt

# Executa o script SQL para criar as tabelas no banco de dados
sudo -u postgres psql -f ../database/schema.sql

echo "Ambiente de desenvolvimento configurado com sucesso!"