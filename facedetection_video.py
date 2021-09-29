import numpy as np
import cv2
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while(True):
# Capture frame-by-frame
    ret, frame = cap.read()
# Our operations on the frame come here
    colored = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Display the resulting frame
    if  cv2.waitKey(1) :# wait 
        faces = faceCascade.detectMultiScale(frame,1.1,4)
        for (x,y,w,h) in faces:
            frame = cv2.rectangle(colored,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow("frame",colored)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()