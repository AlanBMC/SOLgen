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