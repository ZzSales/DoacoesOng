from app import db

# Definição da classe Donor que representa a tabela 'donor' no banco de dados
class Donor(db.Model):
    # Coluna 'id' como chave primária
    id = db.Column(db.Integer, primary_key=True)
    
    # Coluna 'name' para armazenar o nome do doador, não pode ser nula
    name = db.Column(db.String(100), nullable=False)
    
    # Coluna 'email' para armazenar o email do doador, não pode ser nula e deve ser única
    email = db.Column(db.String(100), nullable=False, unique=True)
    
    # Coluna 'cpf' para armazenar o CPF do doador, não pode ser nula e deve ser única
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    
    # Coluna 'created_at' para armazenar a data e hora de criação do registro, com valor padrão como a data e hora atual
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

# Definição da classe Donation que representa a tabela 'donation' no banco de dados
class Donation(db.Model):
    # Coluna 'id' como chave primária
    id = db.Column(db.Integer, primary_key=True)
    
    # Coluna 'donor_id' como chave estrangeira referenciando a tabela 'donor', não pode ser nula
    donor_id = db.Column(db.Integer, db.ForeignKey('donor.id'), nullable=False)
    
    # Coluna 'amount' para armazenar o valor da doação, não pode ser nula
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    
    # Coluna 'donation_date' para armazenar a data e hora da doação, com valor padrão como a data e hora atual
    donation_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # Relacionamento entre as tabelas 'donor' e 'donation'
    donor = db.relationship('Donor', backref=db.backref('donations', lazy=True))