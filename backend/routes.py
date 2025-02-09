from flask import Blueprint, request, jsonify, render_template
from models import Donation, Donor
from app import db

# Criação do blueprint de rotas
routes = Blueprint('routes', __name__)

# Rota para doações
@routes.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        # Verificar se a requisição é JSON ou formulário
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        # Obter dados do doador e da doação
        donor_name = data.get('donor_name')
        email = data.get('email')
        cpf = data.get('cpf')
        amount = data.get('amount')

        # Verificar se todos os campos são obrigatórios
        if not donor_name or not email or not cpf or not amount:
            return jsonify({'error': 'Todos os campos são obrigatórios.'}), 400

        try:
            # Criar instâncias de Donor e Donation
            donor = Donor(name=donor_name, email=email, cpf=cpf)
            donation = Donation(amount=amount, donor=donor)

            # Adicionar e confirmar as instâncias no banco de dados
            db.session.add(donor)
            db.session.add(donation)
            db.session.commit()

            print(f"Doação registrada: {donor_name}, {email}, {cpf}, {amount}")
            return jsonify({'message': 'Doação registrada com sucesso!'}), 201
        except Exception as e:
            # Em caso de erro, reverter a transação
            db.session.rollback()
            print(f"Erro ao registrar a doação: {e}")
            return jsonify({'error': f'Erro ao registrar a doação: {e}'}), 500

    # Renderizar o template donate.html para requisições GET
    return render_template('donate.html')

# Rota para obter todas as doações
@routes.route('/donations', methods=['GET'])
def get_donations():
    # Consultar todas as doações no banco de dados
    donations = Donation.query.all()
    # Retornar as doações em formato JSON
    return jsonify([{'donor': donation.donor.name, 'amount': donation.amount} for donation in donations]), 200