from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from fetchstudentdata import fetchdata


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Student Attendance System")
        root.resizable(0, 0)
        # root.attributes('-alpha', 0.95)

        # Variables for entry field
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_section = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_faculty = StringVar()
        self.var_radio_btn1 = StringVar()

        # Background Image
        imgBg = Image.open(r"images\colorBg.png")
        imgBg = imgBg.resize((1530, 790), Image.ANTIALIAS)
        self.PhoImgBg = ImageTk.PhotoImage(imgBg)  # set image

        BgImg = Label(self.root, image=self.PhoImgBg)  # shows in window
        BgImg.place(x=0, y=0, width=1530, height=790)  # place image

        titleLabel = Label(
            BgImg,
            text="STUDENT MANAGEMENT",
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
            text="STUDENT DETAILS",
            font=("Calibri", 12),
        )
        left_frame.place(x=15, y=10, width=740, height=565)

        img_left = Image.open(r"images\colorBg.png")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.PhoImgLeft = ImageTk.PhotoImage(img_left)

        left_frame_lable = Label(left_frame, image=self.PhoImgLeft)
        left_frame_lable.place(x=5, y=0, width=720, height=80)

        # current course information (student details left side)
        current_course_frame = LabelFrame(
            left_frame,
            bd=3,
            bg="white",
            relief=RIDGE,
            text="CURRENT COURSE INFORMATION",
            font=("Calibri", 12),
        )
        current_course_frame.place(x=5, y=80, width=720, height=150)

        # Department labeling and combobox making
        depart_label = Label(
            current_course_frame, text="Department", font=("Calibri", 13), bg="white"
        )
        depart_label.grid(row=0, column=0, padx=10)

        depart_combo_box = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_dep,
            font=("Calibri", 13),
            state="readonly",
            width=20,
        )
        depart_combo_box["value"] = (
            "select department",
            "ECE",
            "EEE",
            "ETE",
            "CEE",
            "BBA",
            "Economics",
            "Marketing",
            "Law",
        )
        depart_combo_box.current(0)
        depart_combo_box.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course labeling and combobox making
        course_label = Label(
            current_course_frame,
            text="Course",
            font=(
                "Calibri",
                13,
            ),
            bg="white",
        )
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo_box = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_course,
            font=(
                "Calibri",
                13,
            ),
            state="readonly",
            width=20,
        )
        course_combo_box["value"] = ("select course", "CSE 299", "CSE 327", "CSE 373")
        course_combo_box.current(0)
        course_combo_box.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year labeling and combobox making
        year_label = Label(
            current_course_frame,
            text="Year",
            font=(
                "Calibri",
                13,
            ),
            bg="white",
        )
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo_box = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_year,
            font=(
                "Calibri",
                13,
            ),
            state="readonly",
            width=20,
        )
        year_combo_box["value"] = (
            "select year",
            2015,
            2016,
            2017,
            2018,
            2019,
            2020,
            2021,
            2022,
            2023,
            2024,
        )
        year_combo_box.current(0)
        year_combo_box.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester labeling and combobox making
        semester_label = Label(
            current_course_frame,
            text="Semester",
            font=(
                "Calibri",
                13,
            ),
            bg="white",
        )
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo_box = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_semester,
            font=(
                "Calibri",
                13,
            ),
            state="readonly",
            width=20,
        )
        semester_combo_box["value"] = ("select semester", "Summer", "Fall", "Spring")
        semester_combo_box.current(0)
        semester_combo_box.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # University student information
        student_information_frame = LabelFrame(
            left_frame,
            bd=3,
            bg="white",
            relief=RIDGE,
            text="STUDENT INFORMATION",
            font=("Calibri", 12),
        )
        student_information_frame.place(x=5, y=235, width=723, height=303)

        # student Id label and entry field
        studentId_label = Label(
            student_information_frame,
            text="Student ID",
            font=("Calibri", 13),
            bg="white",
        )
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentId_entry_field = ttk.Entry(
            student_information_frame,
            textvariable=self.var_id,
            width=20,
            font=("Calibri", 13),
        )
        studentId_entry_field.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # student name label and entry field
        student_name_label = Label(
            student_information_frame,
            text="Student Name",
            font=("Calibri", 13),
            bg="white",
        )
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_name_entry_field = ttk.Entry(
            student_information_frame,
            textvariable=self.var_name,
            width=20,
            font=(
                "Calibri",
                13,
            ),
        )
        student_name_entry_field.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # student section label and entry field
        student_section_label = Label(
            student_information_frame,
            text="Section",
            font=(
                "Calibri",
                13,
            ),
            bg="white",
        )
        student_section_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        section_combo_box = ttk.Combobox(
            student_information_frame,
            textvariable=self.var_section,
            font=("Calibri", 13),
            state="readonly",
            width=18,
        )

        section_combo_box["value"] = (
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
            "32",
            "33",
            "34",
            "35",
            "36",
            "37",
            "38",
            "39",
            "40"
        )

        section_combo_box.current(0)
        section_combo_box.grid(row=1, column=1, padx=10, pady=5, sticky=W)


        # student Gender label and entry field
        student_gender_label = Label(
            student_information_frame,
            text="Gender",
            font=(
                "Calibri",
                13,
            ),
            bg="white",
        )
        student_gender_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        gender_combo_box = ttk.Combobox(
            student_information_frame,
            textvariable=self.var_gender,
            font=("Calibri", 13),
            state="readonly",
            width=18,
        )

        gender_combo_box["value"] = (
            "Male",
            "Female",
            "Third Gender",
            "Other"
        )

        gender_combo_box.current(0)
        gender_combo_box.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        # student Date of birth label and entry field
        student_birthdate_label = Label(
            student_information_frame,
            text="Birth Date",
            font=("Calibri", 13),
            bg="white",
        )
        student_birthdate_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        student_birthdate_entry_field = ttk.Entry(
            student_information_frame,
            textvariable=self.var_dob,
            width=20,
            font=(
                "Calibri",
                13,
            ),
        )
        student_birthdate_entry_field.grid(row=2, column=1, padx=10, pady=5, sticky=W)


        # student email label and entry field
        student_email_label = Label(
            student_information_frame,
            text="Email",
            font=("Calibri", 13),
            bg="white",
        )
        student_email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        student_email_entry_field = ttk.Entry(
            student_information_frame,
            textvariable=self.var_email,
            width=20,
            font=("Calibri", 13),
        )
        student_email_entry_field.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # student Phone label and entry field
        student_phoneno_label = Label(
            student_information_frame,
            text="Phone No",
            font=("Calibri", 13),
            bg="white",
        )
        student_phoneno_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        student_phoneno_entry_field = ttk.Entry(
            student_information_frame,
            textvariable=self.var_phone,
            width=20,
            font=("Calibri", 13),
        )
        student_phoneno_entry_field.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # student address label and entry field
        student_address_label = Label(
            student_information_frame,
            text="Address",
            font=("Calibri", 13),
            bg="white",
        )
        student_address_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        student_address_entry_field = ttk.Entry(
            student_information_frame,
            textvariable=self.var_address,
            width=20,
            font=("Calibri", 13),
        )
        student_address_entry_field.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # student Faculty label and entry field
        student_instructor_label = Label(
            student_information_frame,
            text="Faculty Name",
            font=("Calibri", 13),
            bg="white",
        )
        student_instructor_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        student_instructor_entry_field = ttk.Entry(
            student_information_frame,
            textvariable=self.var_faculty,
            width=20,
            font=("Calibri", 13),
        )
        student_instructor_entry_field.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # radio buttons

        radio_button1 = ttk.Radiobutton(
            student_information_frame,
            variable=self.var_radio_btn1,
            text="Take Photo Sample",
            value="Yes",
        )
        radio_button1.grid(row=6, column=0)

        radio_button2 = ttk.Radiobutton(
            student_information_frame,
            variable=self.var_radio_btn1,
            text="No Photo Sample",
            value="No",
        )
        radio_button2.grid(row=6, column=1)

        # bbutton frame for student details left side part
        button_frame = Frame(student_information_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=208, width=715, height=35)

        save_btn = Button(
            button_frame,
            text="Save",
            command=self.add_data,
            width=19,
            font=("Calibri", 13, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        save_btn.grid(row=0, column=0)

        update_btn = Button(
            button_frame,
            text="Update",
            command=self.update_data,
            width=19,
            font=("Calibri", 13, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            button_frame,
            text="Delete",
            width=19,
            font=("Calibri", 13, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(
            button_frame,
            text="Reset",
            width=19,
            font=("Calibri", 13, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        reset_btn.grid(row=0, column=3)

        # bbutton frame 2
        button_frame1 = Frame(student_information_frame, bd=2, relief=RIDGE, bg="white")
        button_frame1.place(x=0, y=242, width=715, height=35)

        take_photo_btn = Button(
            button_frame1,
            text="Take Photo Sample",
            width=39,
            font=("Calibri", 13, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(
            button_frame1,
            text="Update Photo Sample",
            width=39,
            font=("Calibri", 13, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        update_photo_btn.grid(row=0, column=1)

        # right label Frame
        right_frame = LabelFrame(
            main_frame,
            bd=3,
            bg="white",
            relief=RIDGE,
            text="STUDENT DETAILS",
            font=("Calibri", 12),
        )
        right_frame.place(x=760, y=10, width=730, height=565)

        img_right = Image.open(r"images\colorBg.png")
        img_right = img_right.resize((710, 130), Image.ANTIALIAS)
        self.PhoImgRight = ImageTk.PhotoImage(img_right)

        right_frame_lable = Label(right_frame, image=self.PhoImgRight)
        right_frame_lable.place(x=5, y=0, width=710, height=80)

        # Search System in right side Student detail
        search_frame = LabelFrame(
            right_frame,
            bd=3,
            bg="white",
            relief=RIDGE,
            text="SEARCH",
            font=("Calibri", 12),
        )
        search_frame.place(x=5, y=80, width=710, height=70)

        search_label = Label(
            search_frame,
            text="Search with: ",
            font=(
                "Calibri",
                15,
            ),
            bg="#A71D31",
            fg="white",
        )
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        semester_label = Label(
            current_course_frame,
            text="Semester",
            font=(
                "Calibri",
                13,
            ),
            bg="white",
        )
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        search_combo_box = ttk.Combobox(
            search_frame,
            font=(
                "Calibri",
                13,
            ),
            state="readonly",
            width=15,
        )
        search_combo_box["values"] = ("Select", "NSU ID", "Phone Number")
        search_combo_box.current(0)
        search_combo_box.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry_field = ttk.Entry(
            search_frame,
            width=15,
            font=(
                "Calibri",
                13,
            ),
        )
        search_entry_field.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(
            search_frame,
            text="Search",
            width=13,
            font=("Calibri", 12, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(
            search_frame,
            text="Show All",
            width=13,
            font=("Calibri", 12, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        showAll_btn.grid(row=0, column=4, padx=4)

        ######## Table Frame #########
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=155, width=710, height=383)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "sec",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "faculty",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        ######## give table dataname #########
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("sec", text="Section")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("faculty", text="Faculty")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        ######## labeling and fixed size to student details right box ########
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=150)
        self.student_table.column("sec", width=75)
        self.student_table.column("gender", width=75)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("faculty", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        fetchdata.FetchStudentData(self)
        self.student_table.bind("<ButtonRelease>", self.FetchCursorDataInEntry)


    # function for add student data

    def add_data(self):
        if (
            self.var_dep.get() == "select department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    username="cse299",
                    password="p2JaZ6@k",
                    database="face_recognition",
                )

                # cursor()=> this is an inbuilt function to execute mysql query
                make_cursor = connection.cursor()
                query = "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                make_cursor.execute(
                    query,
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_section.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_faculty.get(),
                        self.var_radio_btn1.get(),
                    ),
                )

                connection.commit()
                fetchdata.FetchStudentData(self)
                connection.close()
                messagebox.showinfo(
                    "Success", "Student details added successfully", parent=self.root
                )
            except Exception as ex:
                messagebox.showerror("Error", f" Due to : {str(ex)}", parent=self.root)

    """
         FetchCursorDataInEntry ( get the cursor data )this function will work when we click in student data cursor 
         and that time student data will fetch to student details entry fields and show related
         student data . this purpose is ,so tht we can use update function.....
    """

    def FetchCursorDataInEntry(self, event=""):
        focus_on_cursor = self.student_table.focus()
        get_content = self.student_table.item(focus_on_cursor)
        get_data = get_content["values"]

        # data set to entry field
        self.var_dep.set(get_data[0]),
        self.var_course.set(get_data[1]),
        self.var_year.set(get_data[2]),
        self.var_semester.set(get_data[3]),
        self.var_id.set(get_data[4]),
        self.var_name.set(get_data[5]),
        self.var_section.set(get_data[6]),
        self.var_gender.set(get_data[7]),
        self.var_dob.set(get_data[8]),
        self.var_email.set(get_data[9]),
        self.var_phone.set(get_data[10]),
        self.var_address.set(get_data[11]),
        self.var_faculty.set(get_data[12]),
        self.var_radio_btn1.set(get_data[13])


    # Updating funtions
    def update_data(self):
        if (
            self.var_dep.get() == "select department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Update>0:
                    connection = mysql.connector.connect(
                        host="localhost",
                        username="cse299",
                        password="p2JaZ6@k",
                        database="face_recognition",
                    )
                    make_cursor = connection.cursor()
                    make_cursor.execute("update student set Department=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Section=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Faculty=%s, PhotoSample=%s where Student_ID=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_section.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_faculty.get(),
                        self.var_radio_btn1.get(),
                        self.var_id.get()
                    ))
                
                else:
                    if not Update:
                        return
                
                messagebox.showinfo("Success", "Student details have been successfully updated", parent=self.root)
                connection.commit()
                fetchdata.FetchStudentData(self)
                connection.close()

            except Exception as es:
                messagebox.showerror("Error", f"Reason: {str(es)}", parent=self.root)



if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = Student(root)
    root.mainloop()
