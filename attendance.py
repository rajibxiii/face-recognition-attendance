from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from fetchstudentdata import fetchdata
import cv2
import os
import csv
from tkinter import  filedialog

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Student Attendance System")
        root.resizable(0, 0)
        root.attributes("-alpha", 0.95)


        # create variable cz need to show entry field data
        self.var_attend_id = StringVar()
        self.var_attendance_name = StringVar()
        self.var_attend_id_dep = StringVar()






        imgBg = Image.open(r"images\colorBg.png")
        imgBg = imgBg.resize((1530, 790), Image.ANTIALIAS)
        self.PhoImgBg = ImageTk.PhotoImage(imgBg)  # set image

        BgImg = Label(self.root, image=self.PhoImgBg)  # shows in window
        BgImg.place(x=0, y=0, width=1530, height=790)  # place image

        titleLabel = Label(
            BgImg,
            text="ATTENDANCE",
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
            text="ATTENDANCE",
            font=("Calibri", 12),
        )
        left_frame.place(x=15, y=10, width=740, height=565)

        img_left = Image.open(r"images\colorBg.png")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.PhoImgLeft = ImageTk.PhotoImage(img_left)

        left_frame_lable = Label(left_frame, image=self.PhoImgLeft)
        left_frame_lable.place(x=5, y=0, width=720, height=80)

        insideLeftFrame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        insideLeftFrame.place(x=5, y=135, width=720, height=370)

        # Entry - labelland

        # Attendance Id label and entry field
        attendanceId_label = Label(
            insideLeftFrame,
            text="Attendance ID:",
            font=("Calibri", 13),
            bg="white",
        )
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry_field = ttk.Entry(
            insideLeftFrame,
            width=20,
            textvariable= self.var_attend_id,
            font=("Calibri", 13),
        )
        attendanceId_entry_field.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Name label and entry field
        name_label = Label(
            insideLeftFrame,
            text="Name:",
            font=("Calibri", 13),
            bg="white",
        )
        name_label.grid(row=0, column=2, padx=4, pady=8)

        name_entry_field = ttk.Entry(
            insideLeftFrame,
            width=20,
            textvariable=self.var_attendance_name,
            font=("Calibri", 13),
        )
        name_entry_field.grid(row=0, column=3, pady=8)

        # Course label and entry field
        course_label = Label(
            insideLeftFrame,
            text="Course:",
            font=("Calibri", 13),
            bg="white",
        )
        course_label.grid(row=1, column=0)

        course_entry_field = ttk.Entry(
            insideLeftFrame,
            width=20,
            font=("Calibri", 13),
        )
        course_entry_field.grid(row=1, column=1, pady=8)

        # Department label and entry field
        department_label = Label(
            insideLeftFrame,
            text="Department:",
            font=("Calibri", 13),
            bg="white",
        )
        department_label.grid(row=1, column=2)

        department_entry_field = ttk.Entry(
            insideLeftFrame,
            width=20,
            textvariable=self.var_attend_id_dep,
            font=("Calibri", 13),
        )
        department_entry_field.grid(row=1, column=3, pady=8)

        # Date label and entry field
        date_label = Label(
            insideLeftFrame,
            text="Date:",
            font=("Calibri", 13),
            bg="white",
        )
        date_label.grid(row=2, column=0)

        date_entry_field = ttk.Entry(
            insideLeftFrame,
            width=20,
            font=("Calibri", 13),
        )
        date_entry_field.grid(row=2, column=1, pady=8)

        # Time label and entry field
        time_label = Label(
            insideLeftFrame,
            text="Time:",
            font=("Calibri", 13),
            bg="white",
        )
        time_label.grid(row=2, column=2)

        time_entry_field = ttk.Entry(
            insideLeftFrame,
            width=20,
            font=("Calibri", 13),
        )
        time_entry_field.grid(row=2, column=3, pady=8)

        attendance_label = Label(
            insideLeftFrame,
            text="Attendance Status:",
            font=("Calibri", 13),
            bg="white",
        )
        attendance_label.grid(row=3, column=0)

        self.attend_status = ttk.Combobox(
            insideLeftFrame, width=20, font=("Calibri"), state="readonly"
        )
        self.attend_status["values"] = ("Status", "Present", "Absent")
        self.attend_status.grid(row=3, column=1, pady=8)
        self.attend_status.current(0)

        # button frames
        button_frame = Frame(insideLeftFrame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=300, width=715, height=35)

        import_btn = Button(
            button_frame,
            text="Import Data",
            command=self.importFromCsv,
            width=19,
            font=("Calibri", 13, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        import_btn.grid(row=0, column=0)

        export_btn = Button(
            button_frame,
            text="Export Data",
            command=self.exportInCsv,
            width=19,
            font=("Calibri", 13, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        export_btn.grid(row=0, column=1)

        update_btn = Button(
            button_frame,
            text="Update",
            width=19,
            font=("Calibri", 13, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        update_btn.grid(row=0, column=2)

        reset_btn = Button(
            button_frame,
            text="Reset",
            width=19,
            font=("Calibri", 13, "bold"),
            bg="#3F0D12",
            fg="white",
        )
        reset_btn.grid(row=0, column=3)

        # right label Frame
        rightFrame = LabelFrame(
            main_frame,
            bd=3,
            bg="white",
            relief=RIDGE,
            text="ATTENDANCE",
            font=("Calibri", 12),
        )
        rightFrame.place(x=760, y=10, width=730, height=565)

        table_frame = Frame(rightFrame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=710, height=455)

        # Table Scrollbar

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReport = ttk.Treeview(
            table_frame,
            column=("ID", "Name", "Course", "Department", "Date", "Time", "Attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReport.xview)
        scroll_y.config(command=self.AttendanceReport.yview)

        self.AttendanceReport.heading("ID", text="Attendance ID")
        self.AttendanceReport.heading("Name", text="Name")
        self.AttendanceReport.heading("Course", text="Course")
        self.AttendanceReport.heading("Department", text="Department")
        self.AttendanceReport.heading("Date", text="Date")
        self.AttendanceReport.heading("Time", text="Time")
        self.AttendanceReport.heading("Attendance", text="Attendance")

        self.AttendanceReport["show"] = "headings"

        self.AttendanceReport.column("ID", width=100)
        self.AttendanceReport.column("Name", width=100)
        self.AttendanceReport.column("Course", width=100)
        self.AttendanceReport.column("Department", width=100)
        self.AttendanceReport.column("Date", width=100)
        self.AttendanceReport.column("Time", width=100)
        self.AttendanceReport.column("Attendance", width=100)

        self.AttendanceReport.pack(fill=BOTH, expand=1)





    # fetch data of student in attendance window
    """
      ths function will delete 1st get_children data in table and import   
      and insert data from csz file to table
    
    """
    def fetchData(self,rows):
        self.AttendanceReport.delete(*self.AttendanceReport.get_children())
        for data in rows:
            self.AttendanceReport.insert("",END,values=data)

    # import data from CSV file in ATTENDANCE CONSOL
    def importFromCsv(self):
        global mydata
        mydata.clear()
        filename = filedialog.askopenfilename(
            initialdir = os.getcwd(),
            title='Open CSV',
            filetypes=(('CSV File','*.csv'),
                       ("ALL File","*.*")),
            parent=self.root
        )
        with  open(filename) as myfile:
            read_csv = csv.reader(myfile,delimiter=',')
            for data in read_csv:
                mydata.append(data)
            self.fetchData(mydata)

    # export data in CSV FILE

    def exportInCsv(self):
        """
        BY this function we can export data from AttendanceReport to
        another file . so need to Handle error because need to check does
        that file already contain data or not
        """
        try:
            if len(mydata) < 1 :
                messagebox.showerror('No data', " Found no data to export",parent=self.root)
                return False
            filename = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title='Open CSV',
                filetypes=(('CSV File', '*.csv'),
                           ("ALL File", "*.*")),
                parent=self.root
            )
            
            with  open(filename,mode='w',newline="") as myfile:
                csv_write = csv.writer(myfile,delimiter=',')
                for data in mydata:
                    csv_write.writerow(data)
                messagebox.showinfo('Export Data',
                                    'Successfully Data Exported in '+os.path.basename(filename))

        except Exception as ex:
            messagebox.showerror("Error",f'Due to : {str(ex)} ',
                                 parent=self.root)























if __name__ == "__main__":
    root = Tk()  # root is needed to call by toolkit (tk)
    obj = Attendance(root)
    root.mainloop()
