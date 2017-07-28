# import cv2
# import os
# from lab9k.settings import PROJECT_ROOT
#
#
# def recon(now, mtuple):
#     # krijgen map locatie boolean en tupel met x y w h
#
#     x, y, h, w = mtuple
#     x = int(x)
#     y = int(y)
#     h = int(h)
#     w = int(w)
#     # anders zou het crashen
#     if bool:
#         # maakt de facerecon aan
#         recognizer = cv2.createLBPHFaceRecognizer()
#         # de trainer file word in geladen
#         print (os.path.join(PROJECT_ROOT, 'trainer.yml'))
#         recognizer.load(os.path.join(PROJECT_ROOT, 'trainer.yml'))
#         # foto ingeladen
#
#         image = cv2.imread(os.path.join(PROJECT_ROOT, "IMAGES/{}/gray320.jpg".format(now)), 0)
#         # laat het algoritme toe op de foto en dit return een id(uit de
#         # trainner)
#         print(image)
#         print(x, y)
#         id_pers, conf = recognizer.predict(image[y:y + h, x:x + w])
#         # zie trainner
#         if id_pers == 1:
#             id_pers = "Jorg"
#         elif id_pers == 2:
#             id_pers = "Jana"
#         else:
#             id_pers = "Unknown"
#         return id_pers
