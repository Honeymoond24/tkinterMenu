from tkinter import *
from card import *
from header import *


class PageStats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent  # Родительский элемент
        self.controller = controller  # это кто?
        # Фреймы, верстка
        top_frame = Frame(self)
        Header(top_frame, self.controller)
        center = Frame(self)

        # layout all of the main containers
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        self.ctr_left = Frame(center, bg='#00bff6')
        self.ctr_right = Frame(center,
                               # bg="gray",
                               width=512, height=50,
                               padx=20, pady=20)

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.side_bar()
        self.ctr_right.grid(row=0, column=1, sticky="ns")
        # self.cards = Card(self.ctr_right, self.controller, "Корейский суп", 'card1')
        # self.cards1 = Card(self.ctr_right, self.controller, "Корейский суп", 'card2')
        # self.cards2 = Card(self.ctr_right, self.controller, "Корейский суп", 'card3')
        # self.cards.grid(row=0, column=1)
        # self.cards1.grid(row=0, column=2)
        # self.cards2.grid(row=0, column=3)

        # Переменные для боковой панели
        # self.min_w = 50  # Minimum width of the frame
        # self.max_w = 200  # Maximum width of the frame
        # self.cur_width = self.min_w  # Increasing width of the frame
        # self.expanded = False  # Check if it is completely expanded
        self.stats_frame = Frame(self.ctr_right, bg="gray",
                                 width=720, height=360,
                                 padx=20, pady=20)
        self.stats_frame.grid(row=0, column=0)
        self.date_select = tk.Entry(self.ctr_right, width=20)
        self.date_select.grid(row=1, column=0, padx=10, pady=10, sticky='e', rowspan=1)
        # self.stats = tk.Entry(self.ctr_right, width=20)
        # self.stats.grid(row=1, column=0, padx=10, pady=10, sticky='e', rowspan=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)
        print(f"{__name__} loaded")

    def side_bar(self):  # Боковая панель с категориями
        # Make the buttons with the icons to be shown
        btn1 = Button(self.ctr_left,
                      text="Калорийность\nпродуктов",
                      background="#00bff6",  # фоновый цвет кнопки
                      foreground="#F9F9FF",  # цвет текста
                      padx="20",  # отступ от границ до содержимого по горизонтали
                      pady="8",  # отступ от границ до содержимого по вертикали
                      font="16",  # высота шрифта
                      bg='#00bff6',
                      relief='flat',
                      overrelief='flat',
                      activebackground="#00bff6",
                      width=16
                      )
        btn2 = Button(self.ctr_left, text="Блюда чаще всего\nв меню", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16)
        btn3 = Button(self.ctr_left, text="Самые затрачиваемые\nпродукты", background="#896E69", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16)
        btn4 = Button(self.ctr_left, text="Самые популярные\nблюда", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16)
        btn1.grid(row=0, column=0, pady=10)
        btn2.grid(row=1, column=0, pady=10)
        btn3.grid(row=2, column=0, pady=10)
        btn4.grid(row=3, column=0, pady=10)
