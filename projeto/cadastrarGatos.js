// Função para carregar a lista de gatos da API
function carregarGatos() {
    fetch('http://seuservidor.com/api/gatos') // Endpoint da sua API que fornece os dados dos gatos
        .then(response => response.json())
        .then(data => {
            const listaGatos = document.getElementById('lista-gatos');
            listaGatos.innerHTML = ''; // Limpa a lista existente de gatos

            // Adiciona cada gato na lista
            data.forEach(gato => {
                const listItem = document.createElement('li');
                listItem.textContent = `${gato.nome} - ${gato.idade} anos - ${gato.sexo}`;
                listaGatos.appendChild(listItem);
            });
        })
        .catch(error => console.error('Erro ao carregar gatos:', error));
}

// Carrega a lista de gatos ao carregar a página
document.addEventListener('DOMContentLoaded', carregarGatos);