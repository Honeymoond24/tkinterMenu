from tkinter import *
from card import *
from header import *


class PageMain(tk.Frame):
    def __init__(self, parent, controller, database):
        tk.Frame.__init__(self, parent)
        self.parent = parent  # Родительский элемент
        self.controller = controller  # это кто?
        self.database = database
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
        self.ctr_right = Frame(center, padx=3, pady=3)

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.side_bar()
        self.ctr_right.grid(row=0, column=1, sticky="ns")

        self.lb1 = tk.Label(self.ctr_right, text="Поиск:")
        self.lb1.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.search_entry = tk.Entry(self.ctr_right, width=100)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10, sticky='e', rowspan=1)
        self.btn = tk.Button(self.ctr_right, text="Поиск", width=10,
                             command=lambda:
                             self.type_select(f"SELECT * FROM dish WHERE 'dish_name' = '{self.search_entry.get()}'"))
        self.btn.grid(row=0, column=2, padx=10, pady=10, rowspan=1)

        self.cards_frame = Frame(self.ctr_right, height=50)
        self.cards_frame.grid(row=1, column=0, columnspan=10)
        self.data = self.database.select("SELECT * FROM dish")
        print(self.data)
        self.myArray = []
        # self.cards = Card(self.cards_frame, self.controller, self.data[0][1], 'card1')
        # self.cards1 = Card(self.cards_frame, self.controller, self.data[1][1], 'card2')
        # self.cards2 = Card(self.cards_frame, self.controller, self.data[2][1], 'card3')
        # self.cards.grid(row=0, column=1)
        # self.cards1.grid(row=0, column=2)
        # self.cards2.grid(row=0, column=3)
        # self.scrollbary = Scrollbar(self.cards_frame)
        # self.scrollbary.grid(row=0, column=3, rowspan=len(self.data), sticky="ns")
        # textbox = Text(text="2")
        # textbox.pack()
        # textbox.yview
        # self.scroll = Scrollbar(self.cards_frame)
        # self.scroll.grid(row=0, column=3, rowspan=len(self.data), sticky="ns")
        # self.scroll['command'] = self.cards_frame.yview
        # self.textbox['yscrollcommand'] = self.scroll.set
        self.myArray = []

        self.r = 0
        for i in range(len(self.data)):
            j = i % 2

            if i % 2 == 0:
                self.r += 1
            self.myArray.append(
                Card(self.cards_frame, self.controller, self.database, self.data[i][1], self.data[i][0]).grid(
                    row=self.r, column=j,
                    sticky="w")
            )

        # Переменные для боковой панели
        # self.min_w = 50  # Minimum width of the frame
        # self.max_w = 200  # Maximum width of the frame
        # self.cur_width = self.min_w  # Increasing width of the frame
        # self.expanded = False  # Check if it is completely expanded
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)
        print(f"{__name__} loaded")

    def side_bar(self):  # Боковая панель с категориями
        # Make the buttons with the icons to be shown
        btn0 = Button(self.ctr_left, text="Все", background="#896E69", foreground="#D55448", activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', highlightthickness=0, width=16,
                      command=lambda: self.type_select("SELECT * FROM dish"))
        btn1 = Button(self.ctr_left,
                      text="Первые блюда",
                      background="#00bff6",  # фоновый цвет кнопки
                      foreground="#F9F9FF",  # цвет текста
                      padx="20",  # отступ от границ до содержимого по горизонтали
                      pady="8",  # отступ от границ до содержимого по вертикали
                      font="16",  # высота шрифта
                      bg='#00bff6',
                      relief='flat',
                      overrelief='flat',
                      activebackground="#00bff6",
                      width=16, command=lambda: self.type_select("SELECT * FROM dish WHERE type = 'first'")
                      )
        btn2 = Button(self.ctr_left, text="Вторые блюда", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16,
                      command=lambda: self.type_select("SELECT * FROM dish WHERE type = 'second'"))
        btn3 = Button(self.ctr_left, text="Салаты", background="#896E69", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16,
                      command=lambda: self.type_select("SELECT * FROM dish WHERE type = 'salat'"))
        btn4 = Button(self.ctr_left, text="Закуски", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16,
                      command=lambda: self.type_select("SELECT * FROM dish WHERE type = 'snack'"))
        btn5 = Button(self.ctr_left, text="Десерт", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16,
                      command=lambda: self.type_select("SELECT * FROM dish WHERE type = 'dessert'"))
        btn6 = Button(self.ctr_left, text="Напитки", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16,
                      command=lambda: self.type_select("SELECT * FROM dish WHERE type = 'drink'"))
        btn0.grid(row=0, column=0, pady=10)
        btn1.grid(row=1, column=0, pady=10)
        btn2.grid(row=2, column=0, pady=10)
        btn3.grid(row=3, column=0, pady=10)
        btn4.grid(row=4, column=0, pady=10)
        btn5.grid(row=5, column=0, pady=10)
        btn6.grid(row=6, column=0, pady=10)

    def type_select(self, select):
        self.cards_frame.destroy()
        self.cards_frame = Frame(self.ctr_right)
        self.cards_frame.grid(row=1, column=0, columnspan=3)
        self.data = self.database.select(select)
        self.myArray = []
        self.r = 0
        for i in range(len(self.data)):
            j = i % 2
            if i % 2 == 0:
                self.r += 1
            self.myArray.append(
                Card(self.cards_frame, self.controller, self.database, self.data[i][1], self.data[i][0]).grid(row=self.r, column=j,
                                                                                               sticky="w"))
