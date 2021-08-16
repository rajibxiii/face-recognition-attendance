from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from fetchstudentdata import fetchdata
import cv2


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Student Attendance System")
        root.resizable(0, 0)
        root.attributes('-alpha', 0.95)

        imgBg = Image.open(r"images\colorBg.png")
        imgBg = imgBg.resize((1530, 790), Image.ANTIALIAS)
        self.PhoImgBg = ImageTk.PhotoImage(imgBg)  # set image

        BgImg = Label(self.root, image=self.PhoImgBg)  # shows in window
        BgImg.place(x=0, y=0, width=1530, height=790)  # place image


        titleLabel = Label(
            BgImg,
            text="ATTENDANCE",
            font=(
                "Calibri Light",
                30,
            ),
            bg="#E8F0F2",
            fg="black",
        )
        titleLabel.place(x=0, y=120, width=1530, height=50)

        main_frame = Frame(BgImg, bd=2, bg="white")
        main_frame.place(x=10, y=182, width=1505, height=592)

        # left label Frame
        left_frame = LabelFrame(
            main_frame,
            bd=3,
            bg="white",
            relief=RIDGE,
            text="ATTENDANCE",
            font=("Calibri", 12),
        )
        left_frame.place(x=15, y=10, width=740, height=565)

        img_left = Image.open(r"images\colorBg.png")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.PhoImgLeft = ImageTk.PhotoImage(img_left)

        left_frame_lable = Label(left_frame, image=self.PhoImgLeft)
        left_frame_lable.place(x=5, y=0, width=720, height=80)

        # right label Frame
        right_frame = LabelFrame(
            main_frame,
            bd=3,
            bg="white",
            relief=RIDGE,
            text="ATTENDANCE",
            font=("Calibri", 12),
        )
        right_frame.place(x=760, y=10, width=730, height=565)


if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = Attendance(root)
    root.mainloop()
