from tkinter import *
# from tkinter import ttk
from PIL import Image, ImageTk


class FaceRecSys:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
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
        img3 = img3.resize((550, 130), Image.ANTIALIAS)
        self.PhoImg3 = ImageTk.PhotoImage(img3)

        FirstLabel = Label(self.root, image=self.PhoImg3)
        FirstLabel.place(x=1000, y=0, width=530, height=130)

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

        """
          making  button for  'Student Details',' Face Detector' ,
         'Train Data',' Attendance' , 'Photos', 'Exit' 
        """
        #student button(img4)
        StudentBtn = Image.open(r"images\StudentButton.jpg")
        StudentBtn = StudentBtn.resize((130,130),Image.ANTIALIAS)
        self.PhoImgStdBtn = ImageTk.PhotoImage(StudentBtn)

        Btn1 = Button(BgImg , image=self.PhoImgStdBtn, cursor='hand2')
        Btn1.place(x=200 , y=100 , width=130,height=130)

        Btn1 = Button(BgImg, text='Student detail', cursor='hand2',
                      font=("times new Roman", 12, 'bold',),
                      bg='darkblue', fg='white')
        Btn1.place(x=200, y=200, width=129, height=30)

        # Face Detect Button (img5)

        FacDetactBtn = Image.open(r"images\facedetact.PNG")
        FacDetactBtn = FacDetactBtn.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgFacDetBtn = ImageTk.PhotoImage(FacDetactBtn)

        Btn2 = Button(BgImg, image=self.PhoImgFacDetBtn, cursor='hand2')
        Btn2.place(x=450, y=100, width=130, height=130)

        Btn2 = Button(BgImg, text='Face detact', cursor='hand2',
                      font=("times new Roman", 12, 'bold',),
                      bg='darkblue', fg='white')
        Btn2.place(x=450, y=200, width=129, height=30)





if __name__ == "__main__":
    root = Tk()#root is needed to call by toolkit (tk)
    obj = FaceRecSys(root)
    root.mainloop()