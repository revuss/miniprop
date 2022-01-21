from tkinter import font
from turtle import bgcolor
import numpy as np
import face_recognition
import cv2
from tkinter import *
from datetime import datetime
from PIL import Image,ImageTk
import os

window = Tk()
window.title('PROJECT GUI')
window.geometry('720x580')
window.configure(bg="#FFE5D9")
Label(window,text ="Attendance Application",font=("HK Grotesk",25,"bold"),bg="#FFE5D9",fg="#353535").pack()
# print(font.families())
f1 = LabelFrame(window,bg="#FFE5D9")
f1.pack()
L1 = Label (f1,bg="#FFE5D9")
L1.pack()
Button(window,text="VErIfY",font=("HK Grotesk",20,"bold"),bg="#FFE5D9",fg="#353535").pack()


path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
# print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
encodeListKnown = findEncodings(images)    
# print(encodeListKnown.shape)    

face_cascade = cv2.CascadeClassifier('hr.xml')
# def imgconvert(img):
#     image = img.copy()
#     gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#     box,detection = face_cascade.detectMultiScale2(image,minNeighbors =5)

#     # for x,y,w,h in box:
#     #     image=cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
#     # return image


def facerecog(img,recog):
    image = img.copy()
    encode = face_recognition.face_encodings(image,recog)
    return encode




cap = cv2.VideoCapture(0)

while True:
    check,img = cap.read()
    # cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    real = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    box , detection = face_cascade.detectMultiScale2(img,minNeighbors =5)
    for x,y,w,h in box:
        cv2.rectangle(real,(x,y),(x+w,y+h),(0,255,0),2)
    # img = imgconvert(img)
    # img = img
    # enco = facerecog(img)
    # enco = facerecog(img1,img)

    
    # # result = face_recognition.compare_faces([encodeListKnown],enco)
    # # print(result)

    img = ImageTk.PhotoImage(Image.fromarray(real))
    L1['image']= img

    window.update()


cap.release()
window.mainloop()
