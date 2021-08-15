from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from fetchstudentdata import fetchdata
import cv2
import os


class Traindata:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Student Attendance System")
        root.resizable(0, 0)
        root.attributes('-alpha', 0.95)


        titleLabel = Label(
            self.root,
            text="TRAIN DATA SET",
            font=(
                "Calibri Light",
                30,
            ),
            bg="#E8F0F2",
            fg="black",
        )
        titleLabel.place(x=0, y=120, width=1530, height=50)


        img_top = Image.open(r"images\traindata.gif")
        img_top = img_top.resize((1530, 790), Image.ANTIALIAS)
        self.PhoImgTop = ImageTk.PhotoImage(img_top)

        left_frame_lable = Label(self.root, image=self.PhoImgTop)
        left_frame_lable.place(x=0, y=0, width=1530, height=790)


        # Train Data Button
        Btn1 = Button(
            self.root,
            text="TRAIN DATA",
            cursor="hand2",
            font=(
                "Calibri",
                30,
                "bold",
            ),
            bg="#3F0D12",
            fg="white",
        )
        Btn1.place(x=0, y=380, width=1530, height=60)

    
    def trainClassifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') # Converting image to greyscale
            




if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = Traindata(root)
    root.mainloop()


