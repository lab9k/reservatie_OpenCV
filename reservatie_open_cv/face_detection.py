import os
from datetime import datetime
from time import sleep
from lab9k.settings import PROJECT_ROOT

import cv2
from picamera import PiCamera

# store it global to prevent out of resources
camera = PiCamera()

# this methode get called after your date and room is decided
def take_picture():
    # Take a fixed time to create a folder
    now = datetime.now()
    os.makedirs(os.path.join(PROJECT_ROOT, "IMAGES/{}".format(now)))
    # decide the resolution and give the people some time to prepare them
    camera.resolution = (1280, 960)
    sleep(2)
    # Take a picture and put it in your folder
    camera.capture(
        os.path.join(PROJECT_ROOT, "IMAGES/{}/color.jpg".format(now)))
    # we reopen the image to detect faces
    # saving and reopening seems useless but we want one in 1280x960(good
    # quality) and bad quality, so if someone violated the system
    # we have decent proof
    img = cv2.imread(
        os.path.join(PROJECT_ROOT, "IMAGES/{}/color.jpg".format(now)), 0)
    image = cv2.resize(img, (340, 280))
    # Save the cropped one
    cv2.imwrite(
        os.path.join(PROJECT_ROOT, "IMAGES/{}/gray320.jpg".format(now)), image)
    # load the algoritme and try to detect some faces
    face_cascade = cv2.CascadeClassifier(
        '/usr/share/opencv/haarcascades/haarcascade_frontalface_alt2.xml')
    faces = face_cascade.detectMultiScale(image, 1.1, 5)
    # if we detect one we will let the people now by else we say something
    # went wrong
    if len(faces) != 0:
        # we only need 2 things for the face recognition and 1 thing(succes)
        # for interaction of the app
        return {'Time': str(now), 'Success': 'True',
                'Coords': {'x': faces[0].item(0),
                           'y': faces[0].item(1),
                           'h': faces[0].item(2),
                           'w': faces[0].item(3)}}
    return {'Time': str(now), 'Success': 'False', 'Coord': ()}
