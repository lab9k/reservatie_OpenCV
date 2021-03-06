$.ajax({
    type: "POST",
    url: "/camera/",
    success: function (dataCam) {
        //ajax call --> calls the face_detection.py script to take a picture and search a face in it
        //result is something like : {success: true, image: img}
        if (dataCam.Success === "True") {
            //photo has been made
            document.getElementById("textCam").innerHTML = "De foto werd genomen. We zoeken naar uw gegevens.";
            $.ajax({
                type: "post",
                url: "/facerec/",
                data: dataCam,
                success: function (dataFr) {
                    if (dataFr.naam === "None")
                        window.location.assign('/noPerson');
                    else
                        window.location.assign("/confirmation/");
                }
            });

        } else {
            //error occurred while taking a picture --> going to error screen
            window.location.assign("/error/");
        }

    }
});


function wait(ms) {
    var start = new Date().getTime();
    var end = start;
    while (end < start + ms) {
        end = new Date().getTime();
    }
}