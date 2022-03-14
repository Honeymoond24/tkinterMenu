from tkinter import *
from card import Card
from header import *


class DailyMenu(tk.Frame):  # Класс.
    def __init__(self, parent, controller):  # Конструктор ежедневного меню.
        tk.Frame.__init__(self, parent)
        self.controller = controller

        top_frame = Frame(self)
        Header(top_frame, self.controller)  # Шапочка.
        top_frame.grid(row=0, sticky="EW")
        self.center = Frame(self)
        self.center.grid(row=1, column=0, sticky="ns")

        self.label = tk.Label(self.center, background='#FD974F', foreground="#FEF2E4",
                              text="Блюда на сегодня", font=controller.title_font)
        self.label1 = tk.Label(self.center, background='#FD974F', foreground="#FEF2E4",
                               text="Блюда на завтра", font=controller.title_font)
        self.cards = Card(self.center, self.controller, "Суп", 'card1')
        self.cards1 = Card(self.center, self.controller, "Яичница", 'card2')
        self.cards2 = Card(self.center, self.controller, "Овсяная каша", 'card3')
        self.label.grid(row=0, column=0, columnspan=3, sticky="NSEW")
        self.cards.grid(row=1, column=1)
        self.cards1.grid(row=2, column=1)
        self.cards2.grid(row=3, column=1)
        self.cards3 = Card(self.center, self.controller, "Суп", 'card1')
        self.cards4 = Card(self.center, self.controller, "Яичница", 'card2')
        self.cards5 = Card(self.center, self.controller, "Овсяная каша", 'card3')
        self.cards3.grid(row=1, column=2)
        self.cards4.grid(row=2, column=2)
        self.cards5.grid(row=3, column=2)

        self.cards6 = Card(self.center, self.controller, "Суп", 'card1')
        self.cards7 = Card(self.center, self.controller, "Яичница", 'card2')
        self.cards8 = Card(self.center, self.controller, "Овсяная каша", 'card3')
        self.label1.grid(row=0, column=3, columnspan=4, sticky="NSEW")
        self.cards6.grid(row=1, column=3)
        self.cards7.grid(row=2, column=3)
        self.cards8.grid(row=3, column=3)
        self.cards9 = Card(self.center, self.controller, "Суп", 'card1')
        self.cards10 = Card(self.center, self.controller, "Яичница", 'card2')
        self.cards11 = Card(self.center, self.controller, "Овсяная каша", 'card3')
        self.cards9.grid(row=1, column=4)
        self.cards10.grid(row=2, column=4)
        self.cards11.grid(row=3, column=4)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=10)
        # self.parent.grid_rowconfigure(1, weight=1)
        # self.parent.grid_columnconfigure(0, weight=10)
