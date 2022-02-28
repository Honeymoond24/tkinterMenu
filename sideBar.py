from tkinter import *


class SideBar(Tk):
    def __init__(self, parent):
        self.sideMenu = Frame(parent)

        # menu list

        self.fill()

    def fill(self):
        for i in range(10):
            but = Button(self.sideMenu, borderwidth=10)
            but["text"] = str(i) + "_" + str(0)
            but.bind("<Button-1>")
            but.grid(row=i, column=0)
            # but.bind("<Button-1>", lambda event, but=but: changeBut(event, but)) если нужно чтобы каждая кнопка вызывала функцию

        # self.home_b = Button(self.sideMenu, bg='orange',relief='flat')
        # self.set_b = Button(self.sideMenu, bg='orange',relief='flat')
        # self.ring_b = Button(self.sideMenu, bg='orange',relief='flat')

        self.sideMenu.pack()

        # self.home_b.grid(row=0,column=0,pady=10)
        # self.set_b.grid(row=1,column=0,pady=50)
        # self.ring_b.grid(row=2,column=0)
        # self.home_b.config(text='Home',image='',font=(10))
        # self.set_b.config(text='Settings',image='',font=(10))
        # self.ring_b.config(text='Bell Icon',image='',font=(10))
