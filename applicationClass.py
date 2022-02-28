from tkinter import *

from foodcard import Foodcard
from menu import AppMenu
import tkinter.ttk as ttk

from sideBar import SideBar


class Application(Tk):
    def __init__(self):
        self.root = Tk()
        self.root.title("Ресторан \"Шакал\"")
        # Параметры по умолчанию
        self.fra = Frame(self.root, width=960, height=720, bg="White")

        # main frame
        self.mainFrame_side = Frame(self.fra, width=200, height=800, bg="Grey")
        self.mainFrame_ribbon = Frame(self.fra, width=1100, height=50, bg="Green")
        self.mainFrame_content = Frame(self.fra, width=900, height=750, bg="Red")

        self.menuSide = SideBar(self.mainFrame_side)
        self.cards = Foodcard(self.mainFrame_content)

        self.fra.pack()
        self.mainFrame_side.pack(side=LEFT)
        self.mainFrame_ribbon.pack(side=TOP)
        self.mainFrame_content.pack()

        # 

        self.menu = AppMenu(self.root, self.fra)
        self.menu.add_menu()

    # def notebooks(self):
    #     nb = ttk.Notebook(self.root)
    #     nb.pack(fill='both', expand='yes')
    #     f1 = self.fra = Frame(self.root, width=960, height=720, bg="White")
    #     self.fra.pack()
    #     f2 = Text(self.root)
    #     f3 = Text(self.root)
    #     nb.add(f1, text='page1')
    #     nb.add(f2, text='page2')
    #     nb.add(f3, text='page3')

    def start(self):
        # self.notebooks()

        self.root.mainloop()
