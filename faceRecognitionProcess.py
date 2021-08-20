from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
import datetime



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        
        img_top = Image.open(r"images\colorBg.png")
        img_top = img_top.resize((1530, 790), Image.ANTIALIAS)
        self.PhoImgTop = ImageTk.PhotoImage(img_top)

        left_frame_lable = Label(self.root, image=self.PhoImgTop)
        left_frame_lable.place(x=0, y=0, width=1530, height=790)



        # Date And Time
        def currentTime ():
            string = strftime('%d.%m.%Y ∙ %I:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, currentTime)

        lbl = Label (font = ("Calibri Light", 30), background="#3F0D12", foreground="white")
        lbl.place(x=520, y=42, width=500, height=40)
        currentTime ()


        titleLabel = Label(
            text="FACE RECOGNITION",
            font=("Calibri Light",30),
            bg="#A71D31",
            fg="white",
        )

        titleLabel.place(x=0, y=120, width=1530, height=50)



        # FACE RECOGNITION Button

        trainButton = Image.open(r"images\faceR.jpg")
        trainButton = trainButton.resize((270, 270), Image.ANTIALIAS)
        self.PhoImgTrainButton = ImageTk.PhotoImage(trainButton)

        Btn = Button(self.root, image=self.PhoImgTrainButton, cursor="hand2", command=self.face_recog)
        Btn.place(x=633, y=300, width=270, height=260)

        Btn = Button(
            self.root,
            text="FACE RECOGNITION",
            command=self.face_recog,
            cursor="hand2",
            font=("Calibri", 20),
            bg="#3F0D12",
            fg="white",
        )
        Btn.place(x=633, y=558, width=270, height=50)



    # Function for Face Recognition
    def face_recog(self):
        def drawBoundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):

            # convert image in gray scale
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # features variable is used to take the features from classifier
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
            coord = []

            for (x, y, width, height) in features:
                # create a rectangle
                cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 3)
                id, predict = clf.predict(gray_img[y : y + height, x : x + width])
                confidence = int((100*(1 - predict / 300)))

                connection = mysql.connector.connect(
                    host="localhost",
                    username="cse299",
                    password="p2JaZ6@k",
                    database="face_recognition",
                )


                #cursor()= this is an inbuilt function and used here to execute mysql query
                cursor = connection.cursor()

                cursor.execute("SELECT Name FROM face_recognition.student where Student_ID="+str(id))
                connection.autocommit(True)
                n = cursor.fetchone()
                n = "+".join(cursor)

                cursor.execute("SELECT Student_ID FROM face_recognition.student where Student_ID="+str(id))
                connection.autocommit(True)
                i = cursor.fetchone()
                i = "+".join(cursor)

                cursor.execute("SELECT Course FROM face_recognition.student where Student_ID="+str(id))
                connection.autocommit(True)
                c = cursor.fetchone()
                c = "+".join(cursor)

                cursor.execute("SELECT Department FROM face_recognition.student where Student_ID="+str(id))
                connection.autocommit(True)
                d = cursor.fetchone()
                d = "+".join(cursor)


                #confidence is work how long we know the face and also give a value
                if confidence > 77:
                    cv2.putText(img, f"Name: {n}",(x, y - 75),
                        cv2.FONT_HERSHEY_COMPLEX,.5,(255, 0, 25),1)

                    cv2.putText(img,f"ID: {i}",(x, y - 50),cv2.FONT_HERSHEY_COMPLEX,
                                .5,(255, 0, 25),1,)

                    cv2.putText(img,f"Course: {c}",(x, y - 25),
                                cv2.FONT_HERSHEY_COMPLEX,.5,(255, 0, 25),1)

                    cv2.putText(img,f"Department: {d}",(x, y - 5),
                                cv2.FONT_HERSHEY_COMPLEX,.5,(255, 0, 25),1)


                else:
                    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown person ",(x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,0.5, (255, 0, 25), 1)

                coord = [x, y, width, height]

            return coord

        def Recognize(img, clf, faceCascade):
            coord = drawBoundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, img = video_cap.read()
            img = Recognize(img, clf, faceCascade)
            cv2.imshow('Recognizing Face', img)
            cv2.waitKey(1)

            if cv2.getWindowProperty('Recognizing Face', 4) < 1:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = Face_Recognition(root)
    root.mainloop()
