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

        # layout all of the main containers
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=10)

        top_frame.grid(row=0, sticky="EW")
        center.grid(row=1, sticky="NS")
        ctr_left = Frame(center, bg='#FEF2E4')
        ctr_mid = Frame(center, bg='#FEF2E4')
        ctr_right = Frame(center, bg='#FEF2E4')
        ctr_left.grid(row=1, column=0, sticky="EW")
        ctr_mid.grid(row=1, column=1, sticky="EW")
        ctr_right.grid(row=1, column=2, sticky="EW")
        # center.grid_columnconfigure(0, weight=1)
        # center.grid_columnconfigure(1, weight=10)
        # center.grid_columnconfigure(2, weight=1)
        # create the center widgets
        # center.grid_rowconfigure(0, weight=1)
        # center.grid_columnconfigure(1, weight=1)

        # ctr_right = Frame(center, bg='green', padx=3, pady=3)
        self.cards = FoodCard(ctr_mid, self.controller, "продукт 1")
        self.cards1 = FoodCard(ctr_mid, self.controller, "продукт 2")
        self.cards2 = FoodCard(ctr_mid, self.controller, "продукт 3")
        self.cards3 = FoodCard(ctr_mid, self.controller, "продукт 4")
        self.cards4 = FoodCard(ctr_mid, self.controller, "продукт 5")
        self.cards.grid(row=0, column=0)
        self.cards1.grid(row=0, column=1)
        self.cards2.grid(row=0, column=2)
        self.cards3.grid(row=0, column=3)
        self.cards4.grid(row=0, column=4)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)
        # self.grid_columnconfigure(3, weight=1)
        # self.grid_columnconfigure(4, weight=1)

        # ctr_right.grid(row=0, column=2, sticky="ns")