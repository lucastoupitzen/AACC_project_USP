
document.getElementById("enviarbtn").addEventListener("click", capturaInput);


function capturaInput() {

    var numeroUsp = document.getElementById('numeroUsp').value;
    var senha = document.getElementById('senha').value;

    const csrfToken = getCookie("csrftoken");

    console.log("MUdou")

    $.ajax({
        type: 'POST',
        url: '/login',  
        data: {
            'username': numeroUsp,
            'password': senha,
        },
        headers: {
            'X-CSRFToken': csrfToken  // Adicione o token CSRF ao cabeçalho da solicitação
        },
        success: function(response) {

            window.location.href = response;
            // Adicione aqui a lógica para lidar com a resposta da função login
        },
        error: function(error) {
            console.log(error);
        }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Verifica se o cookie começa com o nome desejado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}