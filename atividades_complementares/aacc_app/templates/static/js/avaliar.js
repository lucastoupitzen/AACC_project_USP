$(document).ready(carregarDados());

function carregarDados() {

    const csrfToken = getCookie("csrftoken");

    var informacaoUsuario = document.getElementById("nrousp").innerText;


    $.ajax({
        url: `../../nao_avaliadas/${informacaoUsuario}`,
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
                var linha = $('<tr>');
                linha.append($('<td>').addClass("text-center w-20").text(converterFormatoData(valor.data_envio)));
                linha.append($('<td>').addClass("text-center w-20").text(valor.aluno));
                linha.append($('<td>').addClass("text-center w-20").text("Tipo"));

                var botaoCelulaVisualizar = $('<td>').addClass('text-center w-20');
                var botaoVisualizar = $('<button>').addClass('btn btn-primary visualizar').text('Visualizar');
                botaoCelulaVisualizar.append(botaoVisualizar);
                linha.append(botaoCelulaVisualizar);

                var botaoCelulaAvaliar = $('<td>').addClass('text-center w-20');
                var botaoAvaliar = $('<button>').addClass('btn btn-primary encaminhar').text('Avaliar');
                botaoCelulaAvaliar.append(botaoAvaliar);
                linha.append(botaoCelulaAvaliar);
                
                tabelaCorpo.append(linha);

                // Adicionar evento de clique ao botão
                botaoVisualizar.on('click', function() {
                    abrirArquivoEmNovaAba(valor.doc);
                });

                botaoAvaliar.on('click', function() {
                    abrirModalAvaliar(chave);
                });

            });
        },
        error: function(error) {
            console.error('Erro na requisição:', error);
        }
    });
};

function abrirModalAvaliar(id_aacc) {
    // Atualize o ID da modal conforme necessário
    var modalAvaliar = $('#modalAvaliar');

    modalAvaliar.data('id_aacc', id_aacc);

    // Exiba a modal
    modalAvaliar.modal('show');
}

function confirmarAvaliacao(status) {
    // Aqui, você pode obter o valor do campo de seleção e processar o encaminhamento conforme necessário
    var comentarios = $('#comentarios').val();
    
    var id_AACC = $('#modalAvaliar').data('id_aacc');

    const csrfToken = getCookie("csrftoken");

    $.ajax({
        type: 'POST',
        url: '../../avaliar/',  
        data: {
            'comentarios': comentarios,
            'id_AACC': id_AACC,
            'status': status
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


    // Feche a modal após o processamento
    $('#modalAvaliar').modal('hide');
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