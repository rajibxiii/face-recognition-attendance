from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from fetchstudentdata import fetchdata
import cv2
import os
import numpy as np


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title('Face Recognition System')















if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = FaceRecognition(root)
    root.mainloop()