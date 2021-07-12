from tkinter import *
# from tkinter import ttk
from PIL import Image, ImageTk


class FaceRecSys:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition Student Attendance System')
        root.resizable(0, 0)
        root.attributes('-alpha', 0.95)

        # Background Image
        imgBg = Image.open(
            r"images\colorBg.png")
        imgBg = imgBg.resize((1530, 790), Image.ANTIALIAS)
        self.PhoImgBg = ImageTk.PhotoImage(imgBg)

        BgImg = Label(self.root, image=self.PhoImgBg)
        BgImg.place(x=0, y=0, width=1530, height=790)

        titleLabel = Label(text="Student Attendance System",
                           font=("Calibri Light", 30,),
                           bg='#E8F0F2', fg='black')

        titleLabel.place(x=0, y=120, width=1530, height=50)

        # Making  buttons for 'Student Details', 'Face Detector', 'Train Data', 'Attendance', 'Photos', 'Exit'

        # Student button (img4)
        studenButton = Image.open(r"images\StudentButton.jpg")
        studenButton = studenButton.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgStdBtn = ImageTk.PhotoImage(studenButton)

        Btn1 = Button(BgImg, image=self.PhoImgStdBtn, cursor='hand2')
        Btn1.place(x=200, y=220, width=130, height=130)

        Btn1 = Button(BgImg, text='STUDENT DETAILS', cursor='hand2',
                      font=("Calibri", 12, 'bold',),
                      bg='black', fg='white')
        Btn1.place(x=200, y=320, width=129, height=30)

        # Face Detect Button (img5)
        faceDetectButton = Image.open(r"images\facedetect.PNG")
        faceDetectButton = faceDetectButton.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgFacDetBtn = ImageTk.PhotoImage(faceDetectButton)

        Btn2 = Button(BgImg, image=self.PhoImgFacDetBtn, cursor='hand2')
        Btn2.place(x=450, y=220, width=130, height=130)

        Btn2 = Button(BgImg, text='DETECT FACE', cursor='hand2',
                      font=("Calibri", 12, 'bold',),
                      bg='black', fg='white')
        Btn2.place(x=450, y=320, width=129, height=30)


if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = FaceRecSys(root)
    root.mainloop()
