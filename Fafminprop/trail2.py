import face_recognition
import cv2
import numpy as np
from tkinter import font
from turtle import bgcolor
from tkinter import *
from datetime import datetime
from PIL import Image,ImageTk
import os



# def markup():
#     h = [23,34]
#     markAttendance(name)
# def markAttendance(name):
#      if b1.click():
#         # ClockInButton.setEnabled(False)
#     with open('Attendance.csv','r+') as f:
#         myDataList = f.readlines()
#         nameList = []
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#         if name not in nameList:
#             now = datetime.now()
#             dtString = now.strftime('%H:%M:%S')
#             f.writelines(f'\n{name},{dtString}')




window = Tk()
window.title('PROJECT GUI')
window.geometry('720x580')
window.configure(bg="#FFE5D9")
Label(window,text ="Attendance Application",font=("HK Grotesk",25,"bold"),bg="#FFE5D9",fg="#353535").pack()
f1 = LabelFrame(window,bg="#FFE5D9")
f1.pack()
L1 = Label (f1,bg="#FFE5D9")
L1.pack()
b1 = Button(window,text="VErIfY",font=("HK Grotesk",20,"bold"),bg="#FFE5D9",fg="#353535").pack()


video_capture = cv2.VideoCapture(0)


path = 'ImagesAttendance'
# images = []
# classNames = []
# myList = os.listdir(path)
# print(myList)
# for cl in myList:
#     curImg = cv2.imread(f'{path}/{cl}')
#     images.append(curImg)
#     classNames.append(os.path.splitext(cl)[0])
# print(classNames)
imageload = face_recognition.load_image_file("ImagesAttendance/*.jpg")
# obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
photos = []
for imgs in imageload:
    photos.append(imgs)


my_image = face_recognition.load_image_file("sarath.jpg")
my_face_encoding = face_recognition.face_encodings(my_image)[0]



known_face_encodings = [
    # obama_face_encoding,
    my_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Sarath"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True




while True:
    ret, frame = video_capture.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # markAttendance(name)

    
    img = ImageTk.PhotoImage(Image.fromarray(frame))
    L1['image']= img

    window.update()


video_capture.release()
    
window.mainloop()
