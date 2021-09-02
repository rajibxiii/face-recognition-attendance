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
import webbrowser


class Helpdesk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Contact Us")
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

        lbl = Label (font = ("Calibri Light", 30), background="white", foreground="white")
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


        # Mail Button
        sendMailButton = Image.open(r"images\emaild.jpg")
        sendMailButton = sendMailButton.resize((270, 270), Image.ANTIALIAS)
        self.PhoImgsendMailButton = ImageTk.PhotoImage(sendMailButton)

        Btn = Button(self.root, image=self.PhoImgsendMailButton, cursor="hand2", command=self.sendMail)
        Btn.place(x=632, y=300, width=270, height=270)

        Btn = Button(
            self.root,
            text="EMAIl DEVELOPER",
            command=self.sendMail,
            cursor="hand2",
            font=("Calibri", 20),
            bg="#3F0D12",
            fg="white",
        )
        Btn.place(x=632, y=565, width=270, height=60)   


    
    def sendMail(self):
        webbrowser.open('mailto:md.razib@northsouth.edu?subject=FRSAS Issue')




if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = Helpdesk(root)
    root.mainloop()


