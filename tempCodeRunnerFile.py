
        # Attendance Button
        attendanceButton = Image.open(r"images\attendance.jpg")
        attendanceButton = attendanceButton.resize((130, 130), Image.ANTIALIAS)
        self.PhoImgAttendBtn = ImageTk.PhotoImage(attendanceButton)

        Btn3 = Button(BgImg, image=self.PhoImgAttendBtn, cursor="hand2",command=self.attendanceData,)
        Btn3.place(x=850, y=270, width=130, height=130)

        Btn3 = Button(
            BgImg,
            text="ATTENDANCE",
            command=self.attendanceData,
            cursor="hand2",
            font=("Calibri", 12,"bold"),
            bg="#3F0D12",
            fg="white",
        )
        Btn3.place(x=850, y=370, width=130, height=30)