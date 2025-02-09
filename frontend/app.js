// URL da API para enviar as doações
const apiUrl = 'http://localhost:5000/donate';

// Adicionar um ouvinte de evento ao formulário de doação para capturar o evento de envio
document.getElementById('donationForm').addEventListener('submit', async (event) => {
    // Prevenir o comportamento padrão do formulário (recarregar a página)
    event.preventDefault();

    // Obter os valores dos campos do formulário
    const donorName = document.getElementById('donorName').value;
    const email = document.getElementById('email').value;
    const cpf = document.getElementById('cpf').value;
    const donationAmount = document.getElementById('donationAmount').value;

    // Criar um objeto com os dados da doação
    const donationData = {
        donor_name: donorName,
        email: email,
        cpf: cpf,
        amount: donationAmount
    };

    try {
        // Enviar os dados da doação para a API usando fetch
        const response = await fetch(apiUrl, {
            method: 'POST', // Método HTTP
            headers: {
                'Content-Type': 'application/json' // Tipo de conteúdo
            },
            body: JSON.stringify(donationData) // Converter os dados da doação para JSON
        });

        // Verificar se a resposta da API foi bem-sucedida
        if (response.ok) {
            // Converter a resposta para JSON
            const result = await response.json();
            // Exibir uma mensagem de sucesso
            alert(result.message);
        } else {
            // Converter a resposta de erro para JSON
            const error = await response.json();
            // Exibir uma mensagem de erro
            alert(error.error);
        }
    } catch (error) {
        // Exibir uma mensagem de erro em caso de falha na requisição
        console.error('Erro ao enviar a doação:', error);
        alert('Erro ao enviar a doação. Por favor, tente novamente.');
    }
});