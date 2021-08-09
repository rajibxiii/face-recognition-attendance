from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
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
        self.PhoImgBg = ImageTk.PhotoImage(imgBg) #set image

        BgImg = Label(self.root, image=self.PhoImgBg) # shows in window
        BgImg.place(x=0, y=0, width=1530, height=790) # place image

        titleLabel = Label(text="STUDENT MANAGEMENT",
                           font=("Calibri Light", 30,),
                           bg='#E8F0F2', fg='black')

        titleLabel.place(x=0, y=120, width=1530, height=50)

        main_frame= Frame (BgImg, bd=2, bg="white")
        main_frame.place(x=10, y=182, width=1505, height=592)


        # left label Frame
        left_frame= LabelFrame (main_frame, bd=2, bg="white", relief=RIDGE, text="Student Detals", font=("Calibri", 12))
        left_frame.place(x=15, y=10, width=730, height=560)


        img_left = Image.open(r"images\colorBg.png")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.PhoImgLeft = ImageTk.PhotoImage(img_left)

        left_frame_lable =  Label(left_frame,image=self.PhoImgLeft)
        left_frame_lable.place(x=5,y=0,width=720,height=80)


        # current course information (student details left side)
        current_course_frame = LabelFrame( left_frame, bd=2, bg="white", relief=RIDGE, text="Curent Course Information",
                                font=("Calibri", 12))
        current_course_frame .place(x=5, y=80, width=720, height=150)


        # Department labeling and combobox making
        depart_label = Label(current_course_frame,text="Department",font=('Calibri',13),bg='white')
        depart_label.grid(row=0,column=0,padx=10)

        depart_combo_box=ttk.Combobox(current_course_frame,font=('Calibri',13),state='readonly',width=20)
        depart_combo_box['value']=("select department",'ECE','EEE','ETE','CEE','BBA','Economics','Marketing','Law')
        depart_combo_box.current(0)
        depart_combo_box.grid(row=0,column=1,padx=2,pady=10, sticky=W)


        # Course labeling and combobox making
        course_label = Label(current_course_frame, text="Course", font=('Calibri', 13,), bg='white')
        course_label.grid(row=0, column=2, padx=10,sticky=W)

        course_combo_box = ttk.Combobox(current_course_frame, font=('Calibri', 13,), state='readonly',
                                        width=20)
        course_combo_box['value'] = (
        "select course", 'CSE','EEE','SE' )
        course_combo_box.current(0)
        course_combo_box.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        
        # Year labeling and combobox making

        year_label = Label(current_course_frame, text="Year", font=('Calibri', 13,), bg='white')
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo_box = ttk.Combobox(current_course_frame, font=('Calibri', 13,), state='readonly',
                                        width=20)
        year_combo_box ['value'] = (
            "select year", 2020,2021,2022,2023,2024)
        year_combo_box.current(0)
        year_combo_box.grid(row=1, column=1, padx=2, pady=10, sticky=W)


        # semester labeling and combobox making

        semester_label = Label(current_course_frame, text="Semester", font=('Calibri', 13,), bg='white')
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo_box = ttk.Combobox(current_course_frame, font=('Calibri', 13,), state='readonly',
                                        width=20)
        semester_combo_box['value'] = (
            "select semester", 'summer','fall','spring' )
        semester_combo_box.current(0)
        semester_combo_box.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        # University student information
        student_information_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Student Information",
                                          font=("Calibri", 12))
        student_information_frame.place(x=5, y=235, width=720, height=300)

        #student Id label and entry field
        studentId_label = Label(student_information_frame, text="Student ID", font=('Calibri', 13,), bg='white')
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentId_entry_field = ttk.Entry(student_information_frame,width=20,font=('Calibri', 13,))
        studentId_entry_field.grid(row=0,column=1,padx=10,pady=5, sticky=W)

        # student name label and entry field
        student_name_label = Label(student_information_frame, text="Student Name", font=('Calibri', 13,),
                                bg='white')
        student_name_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        student_name_entry_field = ttk.Entry(student_information_frame, width=20, font=('Calibri', 13,))
        student_name_entry_field.grid(row=0, column=3, padx=10,pady=5, sticky=W)

        # student section label and entry field
        student_section_label = Label(student_information_frame, text="Section", font=('Calibri', 13,),
                                   bg='white')
        student_section_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        student_section_entry_field = ttk.Entry(student_information_frame, width=20, font=('Calibri', 13,))
        student_section_entry_field.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # student Gender label and entry field
        student_gender_label = Label(student_information_frame, text="Gender", font=('Calibri', 13,),
                                   bg='white')
        student_gender_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        student_gender_entry_field = ttk.Entry(student_information_frame, width=20, font=('Calibri', 13,))
        student_gender_entry_field.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # student Date of birth label and entry field
        student_birthdate_label = Label(student_information_frame, text="Birth Date", font=('Calibri', 13,),
                                      bg='white')
        student_birthdate_label .grid(row=2, column=0, padx=10, pady=5, sticky=W)

        student_section_entry_field = ttk.Entry(student_information_frame, width=20,
                                                font=('Calibri', 13,))
        student_section_entry_field.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # student Gmail label and entry field
        student_gmail_label = Label(student_information_frame, text="Email",
                                        font=('Calibri', 13,),
                                        bg='white')
        student_gmail_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        student_gmail_entry_field = ttk.Entry(student_information_frame, width=20,
                                                font=('Calibri', 13,))
        student_gmail_entry_field.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # student Phone label and entry field
        student_phoneno_label = Label(student_information_frame, text="Phone No",
                                    font=('Calibri', 13,),
                                    bg='white')
        student_phoneno_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        student_phoneno_entry_field = ttk.Entry(student_information_frame, width=20,
                                              font=('Calibri', 13,))
        student_phoneno_entry_field.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # student address label and entry field
        student_address_label = Label(student_information_frame, text="Address",
                                      font=('Calibri', 13,),
                                      bg='white')
        student_address_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        student_address_entry_field = ttk.Entry(student_information_frame, width=20,
                                                font=('Calibri', 13,))
        student_address_entry_field.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # student instructor label and entry field
        student_instructor_label = Label(student_information_frame, text="instructor Name",
                                      font=('Calibri', 13,),
                                      bg='white')
        student_instructor_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        student_instructor_entry_field = ttk.Entry(student_information_frame, width=20,
                                                font=('Calibri', 13,))
        student_instructor_entry_field.grid(row=4, column=1, padx=10, pady=5, sticky=W)



        # radio buttons
        radio_button1=ttk.Radiobutton(student_information_frame,text='take photo sample',value='Yes')
        radio_button1.grid(row=6,column=0)

        radio_button2 = ttk.Radiobutton(student_information_frame, text='no photo sample', value='No')
        radio_button2.grid(row=6, column=1)


        #button frame for student details left side part
        button_frame = Frame(student_information_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=0,y=200,width=715,height=70)



        # right label Frame
        right_frame= LabelFrame (main_frame, bd=2, bg="white", relief=RIDGE, text="Student Detals", font=("Calibri", 12))
        right_frame.place(x=755, y=10, width=730, height=560)








if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = Student(root)
    root.mainloop()

    