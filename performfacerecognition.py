from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        # Date And Time
        def currentTime ():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, currentTime)

        lbl = Label (font = ("Calibri Light", 40))
        lbl.place(x=612, y=35, width=300, height=50)
        currentTime ()


        titleLabel = Label(
            self.root,
            text="Face Recognition",
            font=("Calibri Light", 30),
            # bg="#E8F0F2",
            bg="#3F0D12",
            fg="white",
        )
        titleLabel.place(x=0, y=0, width=1530, height=60)

        img_top = Image.open(r"images\traindata.gif")
        img_top = img_top.resize((1530, 700), Image.ANTIALIAS)
        self.PhoImgTop = ImageTk.PhotoImage(img_top)

        left_frame_lable = Label(self.root, image=self.PhoImgTop)
        left_frame_lable.place(x=0, y=55, width=1530, height=700)

        # FACE RECOGNITION Button
        Btn1 = Button(
            self.root,
            text="FACE RECOGNITION",
            command=self.face_recog,
            cursor="hand2",
            font=("Calibri", 30, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        Btn1.place(x=570, y=710, width=400, height=40)

    # Taking attendance
    def attendance_marking(self, name, id, course, department):
        with open("attendance.csv", "r+", newline="\n") as att:
            attDataList = att.readlines()
            nameList = []

            for line in attDataList:
                entry == line.split((","))
                nameList.append(entry[0])

            if (
                ((id not in nameList) and (name not in nameList))
                and (course not in nameList)
                and (department not in nameList)
            ):
                now = datetime.datetime.now()
                d1 = now.strftime("%d.%m.%Y")
                dtString = now.strftime("%H:%M:%S")
                att.writelines(
                    f"\n{id},{name},{course},{department},{dtString},{d1},Present"
                )

    # Function for Face Recognition
    def face_recog(self):
        def drawBoundary(img, classifier, sealeFactor, minNeigbours, color, text, clf):

            # convert image in gray scale
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # features variable is used to take the features from classifire
            features = classifier.detectMultiScale(gray_img, sealeFactor, minNeigbours)
            coord = []

            for (x, y, width, height) in features:
                # create a rectangle
                cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 3)
                id, predict = clf.predict(gray_img[y : y + height, x : x + width])
                confidence = int((100 * (1 - predict / 300)))
                connection = mysql.connector.connect(
                    host="localhost",
                    username="cse299",
                    password="p2JaZ6@k",
                    database="face_recognition",
                )

                # cursor()=> this is an inbuilt function and used here to execute mysql query
                cursor = connection.cursor()

                query_name = "select Name from student where Student_ID=" + str(id)
                cursor.execute(query_name)
                name = cursor.fetchone()
                name = "+".join(name)

                query_id = "select Student_ID from student where Student_ID=" + str(id)
                cursor.execute(query_id)
                id = cursor.fetchone()
                id = "+".join(id)

                query_course = "select Course from student where Student_ID=" + str(id)
                cursor.execute(query_course)
                course = cursor.fetchone()
                course = "+".join(course)

                query_department = (
                    "select Department from student where Student_ID=" + str(id)
                )
                cursor.execute(query_department)
                department = cursor.fetchone()
                department = "+".join(department)

                # confidence is work how long we know the face and also give a value
                if confidence > 77:
                    cv2.putText(img, f"Name: {name}",(x, y - 75),
                        cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3,
                    )

                    cv2.putText(img,f"ID: {id}",(x, y - 55),cv2.FONT_HERSHEY_COMPLEX,
                                0.8,(255, 255, 255),3,
                    )

                    cv2.putText(img,f"Course: {course}",(x, y - 30),
                                cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3,
                    )

                    cv2.putText(img,f"Department: {department}",(x, y - 5),
                                cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3,
                    )

                    self.attendance_marking(id, name, course, department)

                else:
                    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown person unable to detect",(x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,0.8, (255, 255, 255), 3,
                    )

                coord = [x, y, width, height]

            return coord

        def Recognize(img, clf, faceCascade):
            coord = drawBoundary(
                img, faceCascade, 1.1, 10, (255, 25, 2555), "Face", clf
            )
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = Recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()

        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = Face_Recognition(root)
    root.mainloop()
