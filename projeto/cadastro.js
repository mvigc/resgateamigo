document.getElementById("formCadastro").addEventListener("submit", function(event) {
    event.preventDefault();
    
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    // Verifica se o localStorage é suportado pelo navegador
    if (typeof(Storage) !== "undefined") {
        // Verifica se os campos não estão vazios
        if (username.trim() === "" || password.trim() === "") {
            alert("Por favor, preencha todos os campos.");
            return; // Encerra a função sem salvar no localStorage se algum campo estiver vazio
        }
        
        // Salva os dados do usuário no localStorage
        localStorage.setItem("username", username);
        localStorage.setItem("password", password);
        
        // Exibe um alerta de sucesso com detalhes do usuário cadastrado
        alert("Usuário '" + username + "' cadastrado com sucesso!");
    } else {
        // Caso o navegador não suporte localStorage
        alert("Desculpe, seu navegador não suporta armazenamento local.");
    }
});
