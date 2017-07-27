import cv2


def recon(now,tuple):
    # krijgen map locatie boolean en tupel met x y w h

    x, y, w, h = tuple
    # anders zou het crashen
    if bool:
        # maakt de facerecon aan
        recognizer = cv2.createLBPHFaceRecognizer()
        # de trainer file word in geladen
        recognizer.load('trainer.yml')
        # foto ingeladen
        image = cv2.imread("IMAGES/{}/gray320.jpg".format(now), 0)
        # laat het algoritme toe op de foto en dit return een id(uit de
        # trainner)
        id_pers, conf = recognizer.predict(image[y:y + h, x:x + w])
        # zie trainner
        if id_pers == 1:
            id_pers = "Jorg"
        elif id_pers == 2:
            id_pers = "Jana"
        else:
            id_pers = "Unknown"
        return id_pers
