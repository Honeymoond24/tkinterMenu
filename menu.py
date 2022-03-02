from tkinter import *
from sys import exit


class AppMenu(Tk):
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.m = Menu(self.parent)
        # Вкладки меню
        self.menu = Menu(self.m, tearoff=0)  # Меню
        self.theme = Menu(self.m, tearoff=0)  # Тема
        self.screensize = Menu(self.m, tearoff=0)  # Размер экрана
        self.about = Menu(self.m, tearoff=0)  # Справка

    def add_menu(self):
        self.parent.config(menu=self.m)
        # Меню главное меню
        self.m.add_cascade(label="Меню", menu=self.menu)
        self.menu.add_command(label="Выйти", command=exit)
        # # Меню тема
        # self.m.add_cascade(label="Тема", menu=self.theme)
        # self.theme.add_command(label="Белый", command=self.color_white)
        # self.theme.add_command(label="Серый", command=self.color_gray)
        # # Меню размер экрана
        # self.m.add_cascade(label="Размер экрана", menu=self.screensize)
        # self.screensize.add_command(label="640x480", command=self.square)
        # self.screensize.add_command(label="800x600", command=self.rectangle)
        # Меню справка
        self.m.add_cascade(label="Справка", menu=self.about)
        self.about.add_command(label="Поставить оценку", command=lambda: self.parent.show_frame("PageAbout"))
        self.about.add_command(label="О программе", command=lambda: self.parent.show_frame("PageAbout"))

    # def color_white(self):
    #     self.controller.config(bg="#FEF2E4")
    #     self.controller.pack()
    #
    # def color_gray(self):
    #     self.controller.config(bg="black")
    #     self.controller.pack()
    #
    # def square(self):
    #     self.controller.config(width=960)
    #     self.controller.config(height=720)
    #     self.controller.pack()
    #
    # def rectangle(self):
    #     self.controller.config(width=1280)
    #     self.controller.config(height=720)
    #     self.controller.pack()
