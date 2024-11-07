function chargerBillet(){
    console.log("On arrive sur la page")
    fetch(api/getBillets)
    .then(function(){
        console.log("Billets recuperers")
    })
    .catch(function(){
        console.log("Erreur lors du chargement des billets")
    })
}