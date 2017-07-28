# import cv2
# import sqlite3
# 
# 
# def recon(tuple):
#     # krijgen map locatie boolean en tupel met x y w h
#     now, bool, tupel = tuple
#     x, y, w, h = tupel
#     # anders zou het crashen
#     if bool:
#         # maakt de facerecon aan
#         recognizer = cv2.createLBPHFaceRecognizer()
#         # de trainer file word in geladen
#         recognizer.load('trainerAlt2Alt2.yml')
#         # foto ingeladen
#         image = cv2.imread("IMAGES/{}/gray320.jpg".format(now), 0)
#         # laat het algoritme toe op de foto en dit return een id(uit de
#         # trainner)
#         id_pers, conf = recognizer.predict(image[y:y + h, x:x + w])
#         print(conf)
#         # aanpassen !!!!!!!!!
#         if conf > 50 and conf < 120:
#                 conn = sqlite3.connect("db.sqlite3")
#                 c = conn.cursor()
#                 for per in c.execute('SELECT * FROM auth_user WHERE id=?', str(id_pref)):
#                         name = per
#                 conn.close()
#         else:
#                 name = "Unknown"
#         return name
