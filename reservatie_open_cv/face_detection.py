import os
from datetime import datetime
from time import sleep
from lab9k.settings import PROJECT_ROOT

import cv2
from picamera import PiCamera
# global to prevent out of resources
camera = PiCamera()


# neemt een foto
def take_picture():
    # vaste tijd nemen voor folder met foto's
    now = datetime.now()
    # aanmaken van die folder
    os.makedirs(os.path.join(PROJECT_ROOT, "IMAGES/{}".format(now)))
    # aanmaken van camera, resolutie instellen en de mensen 2 seconden geven
    camera.resolution = (1280, 960)
    sleep(2)
    # neemt foto sla die op in de folder
    camera.capture(os.path.join(PROJECT_ROOT, "IMAGES/{}/color.jpg".format(now)))
    # roept functie aan om gezicht te zoeken en return die waarde
    # lees foto in die daarnet is opgeslagen in
    # we slaan de foto op en dan open we hem opnieuw zodanig dat we een
    # goede versie hebben en een om te bewerken
    img = cv2.imread(os.path.join(PROJECT_ROOT, "IMAGES/{}/color.jpg".format(now)), 0)
    image = cv2.resize(img, (340, 280))
    # slaan de cropped en grijze foto op (grijs komt van imread tweede veld)
    cv2.imwrite(os.path.join(PROJECT_ROOT, "IMAGES/{}/gray320.jpg".format(now)), image)
    # laden het algoritme in en passen die toe
    face_cascade = cv2.CascadeClassifier(
        '/usr/share/opencv/haarcascades/haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(image, 1.1, 5)
    # als er een gezicht gedetecteert word dan kunnen we zoeken zo niet terug
    # naar de info
    legetupel = ()
    if len(faces) != 0:
        # om het zo snel mogelijk te maken stuur ik de data van het gezicht
        # door aangezien dit algoritme op 320x240 3 sec nodig heeft
        data = {'Time': str(now), 'Success': 'True', 'Coords': {'x': faces[0].item(0),
                                                                'y': faces[0].item(1),
                                                                'h': faces[0].item(2),
                                                                'w': faces[0].item(3)}}
        return data
    mdict = {'Time': str(now), 'Success': 'False', 'Coord': ()}
    return mdict