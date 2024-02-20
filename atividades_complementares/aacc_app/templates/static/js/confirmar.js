$(document).ready(carregarDados());

function carregarDados() {
    const csrfToken = getCookie("csrftoken");

    $.ajax({
        url: '../confirmar_page/nao_confirmadas',
        type: 'GET',
        dataType: 'json',
        headers: {
            'X-CSRFToken': csrfToken  // Adicione o token CSRF ao cabeçalho da solicitação
        },
        success: function(data) {
            var tabelaCorpo = $('.tabela-corpo');
            tabelaCorpo.empty();

            data =  JSON.parse(data);
            $.each(data, function (chave, valor) {

                let valorText;


                if(valor.avaliacao == "1"){
                    valorText = "Deferida"
                } else {
                    valorText = "Indeferida"
                }

                var linha = $('<tr>');
                linha.append($('<td>').addClass("text-center w-20").text(converterFormatoData(valor.data_envio)));
                linha.append($('<td>').addClass("text-center w-20").text(valorText));
                
                
                var botaoCelulaVisualizar = $('<td>').addClass('text-center w-20');
                var botaoVisualizar = $('<button>').addClass('btn btn-primary visualizar').text('Visualizar');
                botaoCelulaVisualizar.append(botaoVisualizar);
                linha.append(botaoCelulaVisualizar);
                
                var botaoCelulaAvaliacao = $('<td>').addClass('text-center w-20');
                var botaoAvaliacao = $('<button>').addClass('btn btn-primary avaliacao').text('Avaliação');
                botaoCelulaAvaliacao.append(botaoAvaliacao);
                linha.append(botaoCelulaAvaliacao);

                var botaoCelulaConfirmar = $('<td>').addClass('text-center w-20');
                var botaoConfirmar = $('<button>').addClass('btn btn-primary confirmar').text('Confirmar');
                botaoCelulaConfirmar.append(botaoConfirmar);
                linha.append(botaoCelulaConfirmar);
                
                tabelaCorpo.append(linha);

                // Adicionar evento de clique ao botão
                botaoVisualizar.on('click', function() {
                    abrirArquivoEmNovaAba(valor.doc);
                });

                // Adicionar evento de clique ao botão
                botaoAvaliacao.on('click', function() {
                    abrirModalAvaliacao(valor.avaliacao, valor.comentarios)
                });

                botaoConfirmar.on('click', function() {
                    confirmarAvaliacao(chave);
                });

            });
        },
        error: function(error) {
            console.error('Erro na requisição:', error);
        }
    });
};

function abrirModalAvaliacao(avaliacao, comentarios){
    // Atualize o ID da modal conforme necessário
    var modalAvaliacao = $('#modalAvaliacao');

    $("#comentarios").text(comentarios);
    $("#status").text((avaliacao == "1") ? "Deferido" : "Indeferido");

    // Exiba a modal
    modalAvaliacao.modal('show');
}

function abrirModalEncaminhar(id_aacc) {
    // Atualize o ID da modal conforme necessário
    var modalEncaminhar = $('#modalEncaminhar');

    modalEncaminhar.data('id_aacc', id_aacc);

    // Exiba a modal
    modalEncaminhar.modal('show');
}

function confirmarAvaliacao(id_AACC) {
    

    const csrfToken = getCookie("csrftoken");

    $.ajax({
        type: 'POST',
        url: './confirmar',  
        data: {
            'id_AACC': id_AACC
        },
        headers: {
            'X-CSRFToken': csrfToken 
        },
        success: function(response) {

            carregarDados()

        },
        error: function(error) {
            console.log(error);
        }
    });

}

// Função para abrir o arquivo em uma nova aba
function abrirArquivoEmNovaAba(caminhoArquivo) {
    window.open(`../${caminhoArquivo}`, '_blank');
}

function converterFormatoData(dataString) {
    // Cria um objeto Date com a string no formato "YYYY-MM-DD"
    var data = new Date(dataString);

    // Obtém os componentes da data (dia, mês, ano)
    var dia = data.getDate();
    var mes = data.getMonth() + 1; // Mês é baseado em zero, então adicionamos 1
    var ano = data.getFullYear();

    // Formata os componentes para o formato desejado
    var dataFormatada = `${dia}/${mes}/${ano}`;

    return dataFormatada;
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