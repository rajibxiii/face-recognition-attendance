from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from fetchstudentdata import fetchdata
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Traindata:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Student Attendance System")
        root.resizable(0, 0)
        root.attributes('-alpha', 0.95)

        
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
            text="TRAIN DATA SET",
            font=(
                "Calibri Light",
                30,
            ),
            bg="#A71D31",
            fg="white",
        )

        titleLabel.place(x=0, y=120, width=1530, height=50)


        # Train Data Button
        trainButton = Image.open(r"images\attendance.jpg")
        trainButton = trainButton.resize((270, 270), Image.ANTIALIAS)
        self.PhoImgTrainButton = ImageTk.PhotoImage(trainButton)

        Btn = Button(self.root, image=self.PhoImgTrainButton, cursor="hand2", command=self.trainClassifier)
        Btn.place(x=632, y=300, width=270, height=270)

        # Train Data Button
        Btn = Button(
            self.root,
            text="TRAIN DATA",
            command=self.trainClassifier,
            cursor="hand2",
            font=("Calibri", 20),
            bg="#3F0D12",
            fg="white",
        )
        Btn.place(x=632, y=565, width=270, height=60)   


    
    def trainClassifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') # Converting image to greyscale

            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        
        ids = np.array(ids)


        # Training the classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Completed training the data set", parent=self.root)




if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = Traindata(root)
    root.mainloop()


