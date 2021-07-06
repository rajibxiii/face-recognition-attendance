from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class FaceRecSys:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1500x790+0+0')
        self.root.title('Face Recognition Student Attendance System')

        # 1st Image
        img1 = Image.open(
            r"images\color1.jpg")  # Opening image file
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.PhoImg = ImageTk.PhotoImage(img1)

        FirstLabel = Label(self.root, image=self.PhoImg)
        FirstLabel.place(x=0, y=0, width=500, height=130)

        # 2nd Image
        img2 = Image.open(
            r"images\color1.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.PhoImg2 = ImageTk.PhotoImage(img2)

        FirstLabel = Label(self.root, image=self.PhoImg2)
        FirstLabel.place(x=500, y=0, width=500, height=130)

        # 3rd Image
        img3 = Image.open(
            r"images\color1.jpg")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.PhoImg3 = ImageTk.PhotoImage(img3)

        FirstLabel = Label(self.root, image=self.PhoImg3)
        FirstLabel.place(x=1000, y=0, width=500, height=130)

        # Background Image
        imgBg = Image.open(
            r"images\colorBg.jpg")
        imgBg = imgBg.resize((1530, 710), Image.ANTIALIAS)
        self.PhoImgBg = ImageTk.PhotoImage(imgBg)

        BgImg = Label(self.root, image=self.PhoImgBg)
        BgImg.place(x=0, y=130, width=1530, height=710)

        TitleLable = Label(BgImg, text="Student Attendance System",
                        font=("times new Roman", 30, 'bold',),
                        bg='white', fg='black')

        TitleLable.place(x=0, y=0, width=1530, height=50)


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecSys(root)
    root.mainloop()