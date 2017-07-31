import cv2
import os
from lab9k.settings import PROJECT_ROOT
from .models import FaceUser

def recon(now, mtuple):
    # krijgen map locatie boolean en tupel met x y w h

    x, y, h, w = mtuple
    x = int(x)
    y = int(y)
    h = int(h)
    w = int(w)
    # anders zou het crashen
    if bool:
        # maakt de facerecon aan
        recognizer = cv2.createLBPHFaceRecognizer()
        # de trainer file word in geladen
        recognizer.load(os.path.join(PROJECT_ROOT, 'trainerAlt2Alt2.yml'))
        # foto ingeladen

        image = cv2.imread(os.path.join(PROJECT_ROOT, "IMAGES/{}/gray320.jpg".format(now)), 0)
        id_pers, conf = recognizer.predict(image[y:y + h, x:x + w])
        # aanpassen !!!!!!!!!
        if 50 < conf < 120:
            face_id = 1
        else:
            face_id = "Unknown"
        return face_id

