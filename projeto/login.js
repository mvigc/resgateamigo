document.getElementById("formLogin").addEventListener("submit", function(event) {
    event.preventDefault();
    
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    
    // Recupera os dados do localStorage
    var storedUsername = localStorage.getItem("username");
    var storedPassword = localStorage.getItem("password");
    
    // Verifica se os dados fornecidos correspondem aos dados armazenados
    if (username === storedUsername && password === storedPassword) {
        // Login bem-sucedido
        alert("Login bem-sucedido! Clique para ser redirecionado");
        // Redireciona para a página de perfil
        window.location.href = "adm.html"; // Altere "perfil.html" para a página desejada
    } else {
        // Login falhou
        alert("Usuário ou senha incorretos.");
    }
});
