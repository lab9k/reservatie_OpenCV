import os
import cv2
import numpy as np
from PIL import Image

# python2.7
# defineer het algoritme voor herkenning en detecteren
recognizer = cv2.createLBPHFaceRecognizer()
face_cascade = cv2.CascadeClassifier(
    '/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')


#  geef een path naam van waar de foto's zitten
def build_trainer_yml(path):
    # neemt alle van de map en steekt ze in een lijst
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []
    # doorloopt alle fotos en init de faces + ids
    for imagePath in image_paths:
        pil_image = Image.open(imagePath).convert('L')
        image_np = np.array(pil_image, 'uint8')
        my_id = int(os.path.split(imagePath)[-1].split(".")[1])
        my_faces = face_cascade.detectMultiScale(image_np)
        for (x, y, w, h) in my_faces:
            face_samples.append(image_np[y:y + h, x:x + w])
            ids.append(my_id)
    return face_samples, ids


# path aanpassen
faces, Ids = build_trainer_yml("dataImages")
recognizer.train(faces, np.array(Ids))
recognizer.save('trainer.yml')
