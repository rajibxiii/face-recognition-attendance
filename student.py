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
        imgBg = Image.open(r"images\colorBg.png")
        imgBg = imgBg.resize((1530, 790), Image.ANTIALIAS)
        self.PhoImgBg = ImageTk.PhotoImage(imgBg)  # set image

        BgImg = Label(self.root, image=self.PhoImgBg)  # shows in window
        BgImg.place(x=0, y=0, width=1530, height=790)  # place image

        titleLabel = Label(text="STUDENT MANAGEMENT",font=("Calibri Light", 30,),bg='#E8F0F2', fg='black')
        titleLabel.place(x=0, y=120, width=1530, height=50)

        main_frame = Frame(BgImg, bd=2, bg="white")
        main_frame.place(x=10, y=182, width=1505, height=592)


        # left label Frame
        left_frame = LabelFrame(main_frame, bd=3, bg="white",relief=RIDGE, text="Student Detals", font=("Calibri", 12))
        left_frame.place(x=15, y=10, width=740, height=565)

        img_left = Image.open(r"images\colorBg.png")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.PhoImgLeft = ImageTk.PhotoImage(img_left)

        left_frame_lable = Label(left_frame, image=self.PhoImgLeft)
        left_frame_lable.place(x=5, y=0, width=720, height=80)


        # current course information (student details left side)
        current_course_frame = LabelFrame(left_frame, bd=3, bg="white",relief=RIDGE, text="Curent Course Information",font=("Calibri", 12))
        current_course_frame .place(x=5, y=80, width=720, height=150)


        # Department labeling and combobox making
        depart_label = Label(current_course_frame, text="Department", font=('Calibri', 13), bg='white')
        depart_label.grid(row=0, column=0, padx=10)

        depart_combo_box = ttk.Combobox(current_course_frame, font=('Calibri', 13), state='readonly', width=20)
        depart_combo_box['value'] = ("select department", 'ECE', 'EEE', 'ETE', 'CEE', 'BBA', 'Economics', 'Marketing', 'Law')
        depart_combo_box.current(0)
        depart_combo_box.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        # Course labeling and combobox making
        course_label = Label(current_course_frame, text="Course", font=('Calibri', 13,), bg='white')
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo_box = ttk.Combobox(current_course_frame, font=('Calibri', 13,), state='readonly', width=20)
        course_combo_box['value'] = ("select course", 'CSE 299', 'CSE 327', 'CSE 373')
        course_combo_box.current(0)
        course_combo_box.grid(row=0, column=3, padx=2, pady=10, sticky=W)


        # Year labeling and combobox making
        year_label = Label(current_course_frame, text="Year", font=('Calibri', 13,), bg='white')
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo_box = ttk.Combobox(current_course_frame, font=('Calibri', 13,), state='readonly', width=20)
        year_combo_box['value'] = ("select year", 2020, 2021, 2022, 2023, 2024)
        year_combo_box.current(0)
        year_combo_box.grid(row=1, column=1, padx=2, pady=10, sticky=W)


        # semester labeling and combobox making
        semester_label = Label(current_course_frame, text="Semester", font=('Calibri', 13,), bg='white')
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo_box = ttk.Combobox(current_course_frame, font=('Calibri', 13,), state='readonly', width=20)
        semester_combo_box['value'] = ("select semester", 'summer', 'fall', 'spring')
        semester_combo_box.current(0)
        semester_combo_box.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        # University student information
        student_information_frame = LabelFrame(left_frame, bd=3, bg="white", relief=RIDGE, text="Student Information", font=("Calibri", 12))
        student_information_frame.place(x=5, y=235, width=723, height=303)


        # student Id label and entry field
        studentId_label = Label(student_information_frame, text="Student ID", font=('Calibri', 13,), bg='white')
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentId_entry_field = ttk.Entry(student_information_frame, width=20, font=('Calibri', 13,))
        studentId_entry_field.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        # student name label and entry field
        student_name_label = Label(student_information_frame, text="Student Name", font=('Calibri', 13,),bg='white')
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_name_entry_field = ttk.Entry(student_information_frame, width=20, font=('Calibri', 13,))
        student_name_entry_field.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        # student section label and entry field
        student_section_label = Label(student_information_frame, text="Section", font=('Calibri', 13,),bg='white')
        student_section_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        student_section_entry_field = ttk.Entry(student_information_frame, width=20, font=('Calibri', 13,))
        student_section_entry_field.grid(row=1, column=1, padx=10, pady=5, sticky=W)


        # student Gender label and entry field
        student_gender_label = Label(student_information_frame, text="Gender", font=('Calibri', 13,),bg='white')
        student_gender_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        student_gender_entry_field = ttk.Entry(student_information_frame, width=20, font=('Calibri', 13,))
        student_gender_entry_field.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        # student Date of birth label and entry field
        student_birthdate_label = Label(student_information_frame,text="Birth Date", font=('Calibri', 13,), bg='white')
        student_birthdate_label .grid(row=2, column=0, padx=10, pady=5, sticky=W)

        student_section_entry_field = ttk.Entry(student_information_frame, width=20,font=('Calibri', 13,))
        student_section_entry_field.grid(row=2, column=1, padx=10, pady=5, sticky=W)


        # student email label and entry field
        student_email_label = Label(student_information_frame, text="Email",font=('Calibri', 13,),bg='white')
        student_email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        student_email_entry_field = ttk.Entry(student_information_frame, width=20,font=('Calibri', 13,))
        student_email_entry_field.grid(row=2, column=3, padx=10, pady=5, sticky=W)


        # student Phone label and entry field
        student_phoneno_label = Label(student_information_frame, text="Phone No",font=('Calibri', 13,),bg='white')
        student_phoneno_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        student_phoneno_entry_field = ttk.Entry(student_information_frame, width=20,font=('Calibri', 13,))
        student_phoneno_entry_field.grid(row=3, column=1, padx=10, pady=5, sticky=W)


        # student address label and entry field
        student_address_label = Label(student_information_frame, text="Address", font=('Calibri', 13,),bg='white')
        student_address_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        student_address_entry_field = ttk.Entry(student_information_frame, width=20,font=('Calibri', 13,))
        student_address_entry_field.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        # student Faculty label and entry field
        student_instructor_label = Label(student_information_frame, text="Faculty Name", font=('Calibri', 13,), bg='white')
        student_instructor_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        student_instructor_entry_field = ttk.Entry(student_information_frame, width=20, font=('Calibri', 13,))
        student_instructor_entry_field.grid(row=4, column=1, padx=10, pady=5, sticky=W)


        # radio buttons
        radio_button1 = ttk.Radiobutton(student_information_frame, text='Take Photo Sample', value='Yes')
        radio_button1.grid(row=6, column=0)

        radio_button2 = ttk.Radiobutton(student_information_frame, text='No Photo Sample', value='No')
        radio_button2.grid(row=6, column=1)


        # bbutton frame for student details left side part
        button_frame = Frame(student_information_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=0, y=208, width=715, height=35)

        save_btn = Button(button_frame, text='Save', width=19, font=('Calibri', 13,"bold"), bg='blue', fg='white')
        save_btn.grid(row=0, column=0)

        update_btn = Button(button_frame, text='Update', width=19, font=('Calibri', 13,"bold"), bg='blue', fg='white')
        update_btn.grid(row=0, column=1)

        delete_btn = Button(button_frame, text='Delete', width=19, font=('Calibri', 13,"bold"), bg='red', fg='white')
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(button_frame, text='Reset', width=19, font=('Calibri', 13,"bold"), bg='blue', fg='white')
        reset_btn.grid(row=0, column=3)

        # bbutton frame 2
        button_frame1 = Frame(student_information_frame, bd=2, relief=RIDGE, bg='white')
        button_frame1.place(x=0, y=242, width=715, height=35)

        take_photo_btn = Button(button_frame1, text='Take Photo Sample', width=39, font=('Calibri', 13,"bold"), bg='blue', fg='white')
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(button_frame1, text='Update Photo Sample', width=39, font=('Calibri', 13,"bold"), bg='blue', fg='white')
        update_photo_btn.grid(row=0, column=1)


        # right label Frame
        right_frame = LabelFrame(main_frame, bd=3, bg="white", relief=RIDGE, text="Student Detals", font=("Calibri", 12))
        right_frame.place(x=760, y=10, width=730, height=565)

        img_right = Image.open(r"images\colorBg.png")
        img_right = img_right.resize((710, 130), Image.ANTIALIAS)
        self.PhoImgRight = ImageTk.PhotoImage(img_right)

        right_frame_lable = Label(right_frame, image=self.PhoImgRight)
        right_frame_lable.place(x=5, y=0, width=710, height=80)


        # Search System in right side Student detail
        search_frame = LabelFrame(right_frame, bd=3, bg='white', relief=RIDGE, text='Search', font=("Calibri", 12))
        search_frame.place(x=5, y=80, width=710, height=70)

        search_label = Label(search_frame, text="Search with: ",font=('Calibri', 15,),bg='red', fg='white')
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        semester_label = Label(current_course_frame, text="Semester", font=('Calibri', 13,), bg='white')
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        search_combo_box = ttk.Combobox(search_frame, font=('Calibri', 13,), state='readonly', width=15)
        search_combo_box["values"] = ("Select", 'NSU ID', 'Phone Number')
        search_combo_box.current(0)
        search_combo_box.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry_field = ttk.Entry(search_frame, width=15,font=('Calibri', 13,))
        search_entry_field.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text='Search', width=13, font=('Calibri', 12,"bold"), bg='blue', fg='white')
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text='Show All', width=13, font=('Calibri', 12,"bold"), bg='blue', fg='white')
        showAll_btn.grid(row=0, column=4, padx=4)



        ######## Table Frame #########
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg='white')
        table_frame.place(x=5, y=155, width=710, height=383)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table = ttk.Treeview(table_frame,column=("dep", "course", "year", "sem","id", "name", "sec", "dob", "email",  "phone", "address",
                                                              "faculty", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        ######## give table dataname #########
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("sec",text="Section")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("faculty",text="Faculty")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        ######## labeling and fixed size to student details right box ########
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("sec", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("faculty", width=100)
        self.student_table.column("photo", width=150)
        
        self.student_table.pack(fill=BOTH, expand=1)






if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = Student(root)
    root.mainloop()