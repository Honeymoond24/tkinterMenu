from tkinter import *


class Foodcard(Tk):
    def __init__(self, parent):
        self.parent=parent
        self.card = Frame(self.parent, width=100, height=50, border=1)
        self.title = Label(text="123")
        self.image = PhotoImage(file="assets/123.png",width=100,height=100)
        self.card.pack()