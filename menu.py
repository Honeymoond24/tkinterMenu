from tkinter import *


class AppMenu(Tk):
    def __init__(self, root, fra):
        self.root = root
        self.fra = fra
        self.m = Menu(self.root)
        # Вкладки меню
        self.menu = Menu(self.m, tearoff=0)  # Меню
        self.theme = Menu(self.m, tearoff=0)  # Тема
        self.screensize = Menu(self.m, tearoff=0)  # Размер экрана
        self.about = Menu(self.m, tearoff=0)  # Справка

    def add_menu(self):
        self.root.config(menu=self.m)
        # Меню главное меню
        self.m.add_cascade(label="Меню", menu=self.menu)
        self.menu.add_command(label="Выйти", command=exit)
        # Меню тема
        self.m.add_cascade(label="Тема", menu=self.theme)
        self.theme.add_command(label="Белый", command=self.color_white)
        self.theme.add_command(label="Серый", command=self.color_gray)
        # Меню размер экрана
        self.m.add_cascade(label="Размер экрана", menu=self.screensize)
        self.screensize.add_command(label="640x480", command=self.square)
        self.screensize.add_command(label="800x600", command=self.rectangle)
        # Меню справка
        self.m.add_cascade(label="Справка", menu=self.about)
        self.about.add_command(label="Поставить оценку", command=self.square)
        self.about.add_command(label="О программе", command=self.square)

    def color_white(self):
        self.fra.config(bg="White")
        self.fra.pack()

    def color_gray(self):
        self.fra.config(bg="Gray")
        self.fra.pack()

    def square(self):
        self.fra.config(width=960)
        self.fra.config(height=720)
        self.fra.pack()

    def rectangle(self):
        self.fra.config(width=1280)
        self.fra.config(height=720)
        self.fra.pack()
