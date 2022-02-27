from tkinter import *
from menu import AppMenu
import tkinter.ttk as ttk

class Application(Tk):
    def __init__(self):
        self.root = Tk()
        self.root.title("Ресторан \"Шакал\"")
        # Параметры по умолчанию
        self.fra = Frame(self.root, width=960, height=720, bg="White")
        #self.fra.pack()
        self.menu = AppMenu(self.root, self.fra)
        self.menu.add_menu()

    def notebooks(self):
        nb = ttk.Notebook(self.root)
        nb.pack(fill='both', expand='yes')
        f1 = self.fra = Frame(self.root, width=960, height=720, bg="White")
        self.fra.pack()
        f2 = Text(self.root)
        f3 = Text(self.root)

        nb.add(f1, text='page1')
        nb.add(f2, text='page2')
        nb.add(f3, text='page3')

    def start(self):
        self.notebooks()
        self.root.mainloop()
