function addRow() {
    const table = document.getElementById('editableTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    newRow.innerHTML = `
        <td contenteditable="true">Novo Nome</td>
        <td contenteditable="true">email@email.com</td>
        <td contenteditable="true">(XX) XXXX-XXXX</td>
        <td><button class="delete-btn" onclick="deleteRow(this)">Excluir</button></td>
    `;
}

// Função para deletar uma linha
function deleteRow(button) {
    const row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}