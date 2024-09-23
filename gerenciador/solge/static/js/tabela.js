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


        document.getElementById('produtosForm').onsubmit = function() {
            const rows = document.querySelectorAll('tr');
            rows.forEach((row, index) => {
                const nome = row.querySelector('.nome').innerText;
                const codigo = row.querySelector('.codigo').innerText;
                const preco = row.querySelector('.preco').innerText;
        
                // Sincronizando os inputs ocultos com os novos valores editados
                if (row.querySelector(`input[name="nome_${index}"]`)) {
                    row.querySelector(`input[name="nome_${index}"]`).value = nome;
                    row.querySelector(`input[name="codigo_${index}"]`).value = codigo;
                    row.querySelector(`input[name="preco_${index}"]`).value = preco;
                }
            });
        };


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
        