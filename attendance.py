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

        insideLefFrame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        insideLefFrame.place(x=5, y=135, width=720, height=300)

        # Entry - labelland

        # Attendance Id label and entry field
        attendanceId_label = Label(
            insideLefFrame,
            text="Attendance ID:",
            font=("Calibri", 13),
            bg="white",
        )
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry_field = ttk.Entry(
            insideLefFrame,
            width=20,
            font=("Calibri", 13),
        )
        attendanceId_entry_field.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        # Name label and entry field
        name_label = Label(
            insideLefFrame,
            text="Name:",
            font=("Calibri", 13),
            bg="white",
        )
        name_label.grid(row=0, column=2, padx=4, pady=8)

        name_entry_field = ttk.Entry(
            insideLefFrame,
            width=20,
            font=("Calibri", 13),
        )
        name_entry_field.grid(row=0, column=3, pady=8)


        # Student ID label and entry field
        id_label = Label(
            insideLefFrame,
            text="ID:",
            font=("Calibri", 13),
            bg="white",
        )
        id_label.grid(row=1, column=0)

        id_entry_field = ttk.Entry(
            insideLefFrame,
            width=20,
            font=("Calibri", 13),
        )
        id_entry_field.grid(row=1, column=1, pady=8)


        # Department label and entry field
        department_label = Label(
            insideLefFrame,
            text="Department:",
            font=("Calibri", 13),
            bg="white",
        )
        department_label.grid(row=1, column=2)

        department_entry_field = ttk.Entry(
            insideLefFrame,
            width=20,
            font=("Calibri", 13),
        )
        department_entry_field.grid(row=1, column=3, pady=8)


        # Date label and entry field
        date_label = Label(
            insideLefFrame,
            text="Date:",
            font=("Calibri", 13),
            bg="white",
        )
        date_label.grid(row=2, column=0)

        date_entry_field = ttk.Entry(
            insideLefFrame,
            width=20,
            font=("Calibri", 13),
        )
        date_entry_field.grid(row=2, column=1, pady=8)


        # Time label and entry field
        time_label = Label(
            insideLefFrame,
            text="Time:",
            font=("Calibri", 13),
            bg="white",
        )
        time_label.grid(row=2, column=2)

        time_entry_field = ttk.Entry(
            insideLefFrame,
            width=20,
            font=("Calibri", 13),
        )
        time_entry_field.grid(row=2, column=3, pady=8)














if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = Attendance(root)
    root.mainloop()
