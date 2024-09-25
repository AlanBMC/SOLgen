function toggleMenu() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
}
document.getElementById("productCodeInput").focus();

document.getElementById("productCodeInput").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Evita comportamento padrão
        const codigoproduto = event.target.value.trim();
        
        if (codigoproduto !== "") {
            console.log(codigoproduto)
            addcardproduto(codigoproduto)
            event.target.value = ""; // Limpa o input
        }
    }
});
function addcardproduto(codigoproduto) {
    console.log('codigo aqui', codigoproduto);
    fetch("/adicionacard/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": getCookie('csrftoken')
        },
        body: JSON.stringify({ "codigo": codigoproduto })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Sessão atualizada:', data);
       
    })
    .catch(error => {
        console.error('Erro ao atualizar:', error);
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se esse cookie começa com o nome fornecido
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function addCardToPage(nome, preco, codigo) {
    // Cria o elemento do card
    const card = document.createElement('div');
    card.classList.add('produto-card');

    // Adiciona o conteúdo do card
    card.innerHTML = `
        <h3>${nome}</h3>
        <p>Preço: R$ ${preco.toFixed(2)}</p>
        <p>Código: ${codigo}</p>
    `;

    // Adiciona o card à página (supondo que exista uma div com id "cards-container")
    document.getElementById('cards-container').appendChild(card);
}