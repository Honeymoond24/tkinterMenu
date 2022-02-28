from tkinter import *


class Foodcard(Tk):
    def __init__(self, parent):
        # self.cardframe= Frame(parent,width=100,height=50,bg="Blue")
        self.p=parent
        self.fillcard(self.p)
    def fillcard(self,p):
        for i in range(5):
            for j in range(4):
                but = Button(p, borderwidth = 5,width=20,height=5)
                but["text"] = str(i) + "_" + str(0)
                but.bind("<Button-1>")
                but.grid(row = i, column =j )
