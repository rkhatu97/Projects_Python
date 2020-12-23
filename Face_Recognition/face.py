# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:23:23 2020

@author: rkhat
"""


from PIL import Image
import cv2
from tensorflow.keras.models import load_model
import numpy as np
from urllib.request import urlopen as uReq
import cv2
import numpy as np
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input("Enter URL: ")

model = load_model('facefeatures_new_model.h5')

# Loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_extractor(img):
    
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    
    if faces == ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face


video_capture = cv2.VideoCapture(0);
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
while True:
    _, frame = video_capture.read()

    
    face=face_extractor(frame)
    if type(face) is np.ndarray:
        width  = video_capture.get(3) 
        height = video_capture.get(4) 
        print('width, height:', width, height)
        face = cv2.resize(face, (224, 224))
        im = Image.fromarray(face, 'RGB')
        img_array = np.array(im)
        img_array = np.expand_dims(img_array, axis=0)
        pred = model.predict(img_array)
        print(pred)
                     
        name="None matching"
        
        if (pred[0][0]>0.50):
            name='Obama'
        elif (pred[0][1]>0.50):
            name='Prajakta'
        elif (pred[0][2]>0.50):
            name='Rohit'
        cv2.putText(frame,name, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    else:
        cv2.putText(frame,"No face found", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
    out.write(frame)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
out.release()
cv2.destroyAllWindows()