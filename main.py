from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class faceRecognitionSystem:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x790+0+0")
        self.root.title("Face Recognition Student Attendance System")


if __name__ == "__main__":
    root = Tk()
    obj = faceRecognitionSystem(root)
    root.mainloop() 