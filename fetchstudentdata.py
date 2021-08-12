from tkinter import*
import mysql.connector


class fetchdata:

    # fetch student data from mySql database (function)
    def FetchStudentData(self):
        connection = mysql.connector.connect(host='localhost', username='root', password="sourav@123",
                                             database="face_recognition")
        # cursor()=> this is an inbuilt function and used here to execute mysql query
        query = "select * from student"
        cursor = connection.cursor()
        cursor.execute(query)
        # all student data is fetch in fetch_std_data variable
        std_data = cursor.fetchall()

        if len(std_data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for data in std_data:
                self.student_table.insert("", END, values=data)

            connection.commit()  # connection.commit() is used so that data can add continously
        connection.close()