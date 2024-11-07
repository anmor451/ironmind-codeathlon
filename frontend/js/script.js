$('#ul-buy-tickets-btn').click(function () {
    console.log("Bouton appuyé")
    fetch('/api/buy')
    .then(function(){
        alert("Félicitation, vous avez acheté un billet")
    })
    .catch(function(){
        console.log("Erreur, mais bouton fonctionne")
    })
});

$(document).ready(function () {
    const api = '/api/';

    $.ajax({
        url: api + 'items',
        type: 'GET',
        success: function (data) {
            console.log(data);
        },
    });
});