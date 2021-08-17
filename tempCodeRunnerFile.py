        # Date And Time
        def currentTime ():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, currentTime)

        lbl = Label (font = ("Calibri Light", 40))
        lbl.place(x=612, y=35, width=300, height=50)
        currentTime ()