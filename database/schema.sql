-- Criação da tabela 'donors' para armazenar informações dos doadores
CREATE TABLE donors (
    -- Coluna 'id' como chave primária, com incremento automático
    id SERIAL PRIMARY KEY,
    
    -- Coluna 'name' para armazenar o nome do doador, não pode ser nula
    name VARCHAR(100) NOT NULL,
    
    -- Coluna 'email' para armazenar o email do doador, não pode ser nula e deve ser única
    email VARCHAR(100) NOT NULL UNIQUE,
    
    -- Coluna 'created_at' para armazenar a data e hora de criação do registro, com valor padrão como a data e hora atual
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela 'donations' para armazenar informações das doações
CREATE TABLE donations (
    -- Coluna 'id' como chave primária, com incremento automático
    id SERIAL PRIMARY KEY,
    
    -- Coluna 'donor_id' como chave estrangeira referenciando a tabela 'donors', com exclusão em cascata
    donor_id INT REFERENCES donors(id) ON DELETE CASCADE,
    
    -- Coluna 'amount' para armazenar o valor da doação, não pode ser nula
    amount DECIMAL(10, 2) NOT NULL,
    
    -- Coluna 'donation_date' para armazenar a data e hora da doação, com valor padrão como a data e hora atual
    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);