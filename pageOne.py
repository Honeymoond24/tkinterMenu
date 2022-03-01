import tkinter as tk
from tkinter import *

from cms.header import *
from foodcard import FoodCard


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        top_frame = Frame(self)
        Header(top_frame, self.controller)
        center = Frame(self, bg='#FEF2E4')

        top_frame.grid(row=0, sticky="EW")
        center.grid(row=1, column=0, sticky="NS")
        # center.grid_columnconfigure(0, weight=1)
        # center.grid_columnconfigure(1, weight=10)
        # center.grid_columnconfigure(2, weight=1)
        # create the center widgets
        # center.grid_rowconfigure(0, weight=1)
        # center.grid_columnconfigure(1, weight=1)

        # ctr_right = Frame(center, bg='green', padx=3, pady=3)
        self.cards0 = FoodCard(center, self.controller, "Мука")
        self.cards1 = FoodCard(center, self.controller, "Картофель")
        self.cards2 = FoodCard(center, self.controller, "Морковь")
        self.cards3 = FoodCard(center, self.controller, "Гречневая крупа")
        self.cards4 = FoodCard(center, self.controller, "Рис")
        self.cards5 = FoodCard(center, self.controller, "Лук")
        self.cards6 = FoodCard(center, self.controller, "Горох")
        self.cards7 = FoodCard(center, self.controller, "Сельдерей")
        self.cards0.grid(row=0, column=0)
        self.cards1.grid(row=0, column=1)
        self.cards2.grid(row=0, column=2)
        self.cards3.grid(row=0, column=3)
        self.cards4.grid(row=0, column=4)
        self.cards5.grid(row=0, column=5)
        self.cards6.grid(row=0, column=6)
        self.cards7.grid(row=0, column=7)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)

        # layout all of the main containers
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=10)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)
        # self.grid_columnconfigure(3, weight=1)
        # self.grid_columnconfigure(4, weight=1)
