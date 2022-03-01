import tkinter as tk
from tkinter import *
from card import *
from cms.header import *


class PageMain(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent  # Родительский элемент
        self.controller = controller  # это кто?
        # Фреймы, верстка
        top_frame = Frame(self)
        Header(top_frame, self.controller)
        center = Frame(self, bg='gray2', pady=3)

        # layout all of the main containers
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        self.ctr_left = Frame(center, bg='#FFA577')
        # ctr_mid = Frame(center, bg='yellow', padx=3, pady=3)
        ctr_right = Frame(center, bg='green', padx=3, pady=3)

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.side_bar()
        # ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")
        self.cards = Card(ctr_right, self.controller, "карточка1", 'card1')
        self.cards1 = Card(ctr_right, self.controller, "карточка2", 'card2')
        self.cards2 = Card(ctr_right, self.controller, "карточка3", 'card3')
        self.cards.grid(row=0, column=1)
        self.cards1.grid(row=0, column=2)
        self.cards2.grid(row=0, column=3)

        # Переменные для боковой панели
        self.min_w = 50  # Minimum width of the frame
        self.max_w = 200  # Maximum width of the frame
        self.cur_width = self.min_w  # Increasing width of the frame
        self.expanded = False  # Check if it is completely exanded

    def side_bar(self):  # Боковая панель с категориями
        # Make the buttons with the icons to be shown
        btn0 = Button(self.ctr_left, text="Все", background="#896E69", foreground="#ccc", activebackground="#FFA577",
                      padx="20", pady="8", font="16", bg='#FFA577', relief='flat', highlightthickness=0)
        btn0.grid(row=0, column=0, pady=10)
        btn1 = Button(self.ctr_left,
                      text="Первые блюда",
                      background="#FFA577",  # фоновый цвет кнопки
                      foreground="#ccc",  # цвет текста
                      padx="20",  # отступ от границ до содержимого по горизонтали
                      pady="8",  # отступ от границ до содержимого по вертикали
                      font="16",  # высота шрифта
                      bg='#FFA577',
                      relief='flat'
                      )
        btn1.grid(row=1, column=0, pady=10)
        btn_width = btn1.winfo_width()
        print(btn_width)
        btn2 = Button(self.ctr_left, text="Вторые блюда", background="#FFA577", foreground="#ccc",
                      # padx="20",
                      pady="8", font="16", bg='#FFA577', relief='flat')
        btn3 = Button(self.ctr_left, text="Салаты", background="#896E69", foreground="#ccc", activebackground="#FFA577",
                      padx="20", pady="8", font="16", bg='#FFA577', relief='flat', highlightthickness=0)
        btn4 = Button(self.ctr_left, text="Закуски", background="#FFA577", foreground="#ccc",
                      padx="20", pady="8", font="16", bg='#FFA577', relief='flat')
        btn5 = Button(self.ctr_left, text="Десерт", background="#FFA577", foreground="#ccc",
                      padx="20", pady="8", font="16", bg='#FFA577', relief='flat')
        btn6 = Button(self.ctr_left, text="Напитки", background="#FFA577", foreground="#ccc",
                      padx="20", pady="8", font="16", bg='#FFA577', relief='flat')
        btn2.grid(row=2, column=0, pady=10)
        btn3.grid(row=3, column=0, pady=10)
        btn4.grid(row=4, column=0, pady=10)
        btn5.grid(row=5, column=0, pady=10)
        btn6.grid(row=6, column=0, pady=10)
