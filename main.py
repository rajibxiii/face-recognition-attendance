from tkinter import *
# from tkinter import ttk
from PIL import Image, ImageTk


class FaceRecSys:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition Student Attendance System')

        # Background Image
        imgBg = Image.open(
            r"images\colorBg.png")
        imgBg = imgBg.resize((1530, 790), Image.ANTIALIAS)
        self.PhoImgBg = ImageTk.PhotoImage(imgBg)

        BgImg = Label(self.root, image=self.PhoImgBg)
        BgImg.place(x=0, y=0, width=1530, height=790)

        TitleLable = Label(text="Student Attendance System",
                        font=("Calibri Light", 30,),
                        fg='black')

        TitleLable.place(x=0, y=120, width=1530, height=50)

        """
          making  button for  'Student Details',' Face Detector' ,
         'Train Data',' Attendance' , 'Photos', 'Exit' 
        """
        #student button(img4)
        StudentBtn = Image.open(r"images\StudentButton.jpg")
        StudentBtn = StudentBtn.resize((130,130),Image.ANTIALIAS)
        self.PhoImgStdBtn = ImageTk.PhotoImage(StudentBtn)

        Btn1 = Button(BgImg , image=self.PhoImgStdBtn, cursor='hand2')
        Btn1.place(x=200 , y=220 , width=130,height=130)

        Btn1 = Button(BgImg, text='Student detail', cursor='hand2',
                      font=("times new Roman", 12, 'bold',),
                      bg='darkblue', fg='white')
        Btn1.place(x=200, y=320, width=129, height=30)

        # Face Detect Button (img5)

        FacDetactBtn = Image.open(r"images\facedetact.PNG")
        FacDetactBtn = FacDetactBtn.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgFacDetBtn = ImageTk.PhotoImage(FacDetactBtn)

        Btn2 = Button(BgImg, image=self.PhoImgFacDetBtn, cursor='hand2')
        Btn2.place(x=450, y=220, width=130, height=130)

        Btn2 = Button(BgImg, text='Face detact', cursor='hand2',
                      font=("times new Roman", 12, 'bold',),
                      bg='darkblue', fg='white')
        Btn2.place(x=450, y=320, width=129, height=30)





if __name__ == "__main__":
    root = Tk()#root is needed to call by toolkit (tk)
    obj = FaceRecSys(root)
    root.mainloop()