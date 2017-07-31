import cv2
import os
from lab9k.settings import PROJECT_ROOT


def recon(now, mtuple):
    # krijgen map locatie boolean en tupel met x y w h

    x, y, h, w = mtuple
    x = int(x)
    y = int(y)
    h = int(h)
    w = int(w)
    # maakt de facerecognizer aan
    recognizer = cv2.createLBPHFaceRecognizer()
    # de trainer file word in geladen, elke keer als je een nieuw persoon wilt
    # toevoegen moet je de volledige file opnieuw maken
    # door het script uit te voeren (/face_Recognition/build_trainer.py)
    recognizer.load(os.path.join(PROJECT_ROOT, 'trainerAlt2Alt2.yml'))
    # foto ingeladen
    image = cv2.imread(
        os.path.join(PROJECT_ROOT, "IMAGES/{}/gray320.jpg".format(now)), 0)
    id_pers, conf = recognizer.predict(image[y:y + h, x:x + w])
    # geeft het id door zal worden opgehaald in database
    # conf word gebruikt voor meerdere zekerheid van de foto,
    # beter trainen betere waarden
    if not 50 < conf < 120:
        id_pers = "Unknown"
    return id_pers
