import cv2
import os
from lab9k.settings import PROJECT_ROOT


def recon(now, mtuple):
    # we receive a time(string) and a tuple with 4 coordinates, cast everything
    # to the correct type
    x, y, h, w = mtuple
    x = int(x)
    y = int(y)
    h = int(h)
    w = int(w)
    # create a recognizer, we opted for a LBPHFaceRecognizer cause trying this
    # is easyer then Eigenfaces and Fisherfaces
    recognizer = cv2.createLBPHFaceRecognizer()
    # we load the trainer file, if you want to add a person to your trainer
    # in LBPH, you will need a script to rebuild the trainer file
    # script located at /face_Recognition/build_trainer.py
    # Name of trainer.yml is Alt2Alt2 cause the HAAR cascade I used are
    # .../haarcascade_frontalface_alt2.xml
    recognizer.load(os.path.join(PROJECT_ROOT, 'trainerAlt2Alt2.yml'))
    # load image in var
    image = cv2.imread(
        os.path.join(PROJECT_ROOT, "IMAGES/{}/gray320.jpg".format(now)), 0)
    # try to predict who is on the picture
    id_pers, conf = recognizer.predict(image[y:y + h, x:x + w])
    # id for database and conf for % matching, more training = better detecting
    if not 50 < conf < 120:
        id_pers = "Unknown"
    return id_pers
