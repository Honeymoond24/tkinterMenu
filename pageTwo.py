import tkinter as tk
from tkinter import *
from card import Card

from cms.header import *
from foodcard import FoodCard


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        top_frame = Frame(self, pady=3)
        Header(top_frame, self.controller)
        center = Frame(self, bg='#FEF2E4', pady=3)
        # layout all of the main containers
        #self.parent.grid_rowconfigure(0, weight=1)
        #self.parent.grid_columnconfigure(1, weight=2)

        top_frame.grid(row=0, sticky="EW")
       
        center.grid(row=1, sticky="nsew")
        label = tk.Label(center,background='#FD974F', text="Блюда на сегодня", font=controller.title_font)
        label1 = tk.Label(center,background='#FD974F', text="Блюда на Завтра", font=controller.title_font)
        self.cards = Card(center, self.controller, "карточка1", 'card1')
        self.cards1 = Card(center, self.controller, "карточка2", 'card2')
        self.cards2 = Card(center, self.controller, "карточка3", 'card3')
        label.grid(row=0,column=0,columnspan=3,sticky="NSEW")
        self.cards.grid(row=1, column=1)
        self.cards1.grid(row=2, column=1)
        self.cards2.grid(row=3, column=1)
        self.cards3 = Card(center, self.controller, "карточка1", 'card1')
        self.cards4 = Card(center, self.controller, "карточка2", 'card2')
        self.cards5 = Card(center, self.controller, "карточка3", 'card3')
        self.cards3.grid(row=1, column=2)
        self.cards4.grid(row=2, column=2)
        self.cards5.grid(row=3, column=2)

        self.cards6 = Card(center, self.controller, "карточка1", 'card1')
        self.cards7 = Card(center, self.controller, "карточка2", 'card2')
        self.cards8 = Card(center, self.controller, "карточка3", 'card3')
        label1.grid(row=0,column=3,columnspan=4,sticky="NSWE")
        self.cards6.grid(row=1, column=3)
        self.cards7.grid(row=2, column=3)
        self.cards8.grid(row=3, column=3)
        self.cards9 = Card(center, self.controller, "карточка1", 'card1')
        self.cards10 = Card(center, self.controller, "карточка2", 'card2')
        self.cards11 = Card(center, self.controller, "карточка3", 'card3')
        self.cards9.grid(row=1, column=4)
        self.cards10.grid(row=2, column=4)
        self.cards11.grid(row=3, column=4)

        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=10)
        
       
        
