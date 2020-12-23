# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 18:26:00 2020

@author: rkhat
"""


import cv2
import numpy as np
from urllib.request import urlopen as uReq
import cv2
import numpy as np
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
# image_name = input("Image Name: ")
cap = cv2.VideoCapture("http://192.168."+url+":8080/video");
#fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1920, 1080))
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count = 0
def face_dataset(img):
    faces = face_classifier.detectMultiScale(img, 1.3, 5)
    if faces is ():
        return None
    for (x,y,w,h) in faces:
        x=x-10
        y=y-10
        cropped_face = img[y:y+h+50, x:x+w+50]

    return cropped_face
while True:
    ret, frame = cap.read()
    if face_dataset(frame) is not None:
        count += 1
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = cv2.resize(face_dataset(gray), (400, 400))
        file_name_path = 'D:/Spyder/Images/' + str(count) +'.jpg'
        cv2.imwrite(file_name_path, face)

        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('Face Cropper', face)
        
    else:
        print("Face not found")
        pass
           # cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
        
    q = cv2.waitKey(1)
    if q == ord("q") or count == 100:
        break;

cap.release()
cv2.destroyAllWindows()



    

