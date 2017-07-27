$.ajax({
    type: "POST",
    url: "/camera/",
    success: function(data) {
        //hier krijg je data vanuit de camera functie --> indien gelukt verderdoen en indien niet error!
        document.getElementById("textCam").innerHTML = "De foto werd genomen. We zoeken naar uw gegevens.";
    }
});