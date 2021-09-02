        # Background Image
        imgBg = Image.open(r"images\About.jpg")
        imgBg = imgBg.resize((1530, 790), Image.ANTIALIAS)
        self.PhoImgBg = ImageTk.PhotoImage(imgBg)  # set image

        BgImg = Label(self.root, image=self.PhoImgBg)  # shows in window
        BgImg.place(x=0, y=0, width=1530, height=790)  # place image