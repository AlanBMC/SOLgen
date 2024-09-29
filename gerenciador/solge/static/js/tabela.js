function addRow() {
    const table = document.getElementById('editableTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    newRow.innerHTML = `
        <td contenteditable="true">Novo Nome</td>
        <td contenteditable="true">000000000</td>
        <td contenteditable="true">XXXXXXXX</td>
        <td><button class="delete-btn" onclick="deleteRow(this)">Excluir</button></td>
    `;
}

// Função para deletar uma linha
function deleteRow(button) {
    const row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}
function toggleMenu() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
}

        // Abre o modal
        var modal = document.getElementById("myModal");
        var openModalBtn = document.getElementById("openModalBtn");
        var closeBtn = document.getElementsByClassName("close")[0];

        // Quando o usuário clicar no link, abre o modal
        openModalBtn.onclick = function(event) {
            event.preventDefault(); // Impede o comportamento padrão do link
            modal.style.display = "block";
        }

        // Fecha o modal quando o usuário clicar no X
        closeBtn.onclick = function() {
            modal.style.display = "none";
        }

        // Fecha o modal se o usuário clicar fora dele
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }




function sendUpdate(produtoData) {
    fetch("/atualiza_produtos/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie('csrftoken')
        },
        body: JSON.stringify(produtoData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Sessão atualizada:', data);
    })
    .catch(error => {
        console.error('Erro ao atualizar:', error);
    });
}

// Adiciona listener para detectar edições nas células da tabela
document.querySelectorAll('.editable').forEach(cell => {
    cell.addEventListener('blur', function() {
        // Quando o usuário terminar de editar a célula, pegue os dados
        const row = this.closest('tr');
        const produtoData = {
            codigo_de_barras: row.querySelector('.codigo').textContent,
            nome: row.querySelector('.nome').textContent,
            valor_revenda: row.querySelector('.preco').textContent
        };

        // Envie os dados via AJAX para atualizar a sessão
        sendUpdate(produtoData);
    });
});

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
function clicando(){
    setTimeout(function() {
        document.getElementById('arquivo').click();
    }, 1000);
}

document.addEventListener('DOMContentLoaded', function () {
    // Mostra o loader quando o formulário for submetido
    const form = document.querySelector('form');
    const loader = document.getElementById('loader');

    if (form) {
        form.addEventListener('submit', function () {
            // Mostra o loader
            loader.style.display = 'block';
        });
    }

    // Você pode opcionalmente usar window.onload para esconder o loader após a página recarregar.
    window.onload = function() {
        loader.style.display = 'none';
    };
});
