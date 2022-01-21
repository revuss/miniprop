import cv2
import numpy as np 
 
# C= cv2.imread('imgtest.jpg')
face_cascade = cv2.CascadeClassifier('hr.xml')
def imagecls(img):
    image = img.copy()
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)



    box,detection = face_cascade.detectMultiScale2(gray,minNeighbors = 5)

    for x,y,w,h in box:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,2,200),2)
    return image    

cap = cv2.VideoCapture(0)
while True:
    check,frame =cap.read()
    if check == False:
        break
    imageon = imagecls(frame)
    print(imageon)
    cv2.imshow("output",imageon)
    if cv2.waitKey(1) == 27 :
        break
cap.release()
cv2.destroyAllWindows()    

# cv2.imshow("output",cls)
# cv2.waitKey(0)
# cv2.destroyAllWindows()