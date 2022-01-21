import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from tkinter import font
from turtle import bgcolor
from tkinter import *
from PIL import Image,ImageTk


window = Tk()
window.title('PROJECT GUI')
window.geometry('720x580')
window.configure(bg="#FFE5D9")

Label(window,text ="Attendance Application",font=("HK Grotesk",25,"bold"),bg="#FFE5D9",fg="#353535").pack()

f1 = LabelFrame(window,bg="#FFE5D9")
f1.pack()

L1 = Label (f1,bg="#FFE5D9")
L1.pack()

Button(window,text="VErIfY",font=("HK Grotesk",20,"bold"),bg="#FFE5D9",fg="#353535").pack()

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

for img in myList:
    faces = face_recognition.load_image_file(img)
    cv2.imshow("output",faces)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 