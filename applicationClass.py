from tkinter import *
from menu import AppMenu


class Application(Tk):
    def __init__(self):
        self.root = Tk()
        self.root.title("Ресторан \"Шакал\"")
        # Параметры по умолчанию
        self.fra = Frame(self.root, width=960, height=720, bg="White")
        self.fra.pack()
        self.menu = AppMenu(self.root, self.fra)
        self.menu.add_menu()

    def start(self):
        self.root.mainloop()
