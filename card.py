from tkinter import *

class Card(Tk):
    def __int__(self, parent, title, image):
        self.card = Frame(parent, width=100, height=50, border=1)
        self.title = Label(text=title)
        self.image = Image()