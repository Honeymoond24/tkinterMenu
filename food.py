from tkinter import *
from tkinter import ttk
from header import *
from foodcard import FoodCard


class Food(tk.Frame):  # Класс.
    def __init__(self, parent, controller):  # Конструктор Продуктов.
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        top_frame = Frame(self)
        Header(top_frame, self.controller)  # Шапочка.
        center = Frame(self)
        self.ctr_left = Frame(center, bg='#00bff6')
        self.ctr_right = Frame(center, padx=3, pady=3)

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.side_bar()
        self.ctr_right.grid(row=0, column=1, sticky="nse")
        top_frame.grid(row=0, sticky="EW")
        center.grid(row=1, column=0, sticky="nsew")
        self.tree = ttk.Treeview(self.ctr_right, height=15)
        self.table_tree()

        # layout all of the main containers
        # self.parent.grid_rowconfigure(1, weight=1)
        # self.parent.grid_columnconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)
        print(f"{__name__} loaded")

    def table_tree(self):
        self.lb0 = tk.Label(self.ctr_right, text="                                    ")
        self.lb0.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.lb1 = tk.Label(self.ctr_right, text="Поиск:")
        self.lb1.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        self.search_entry = tk.Entry(self.ctr_right, width=100)
        self.search_entry.grid(row=0, column=2, padx=10, pady=10, sticky='e', rowspan=1)
        self.btn = tk.Button(self.ctr_right, text="Поиск", width=10)
        self.btn.grid(row=0, column=3, padx=10, pady=10, rowspan=1)

        self.tree["columns"] = ("one", "two", "three", "four", "five")
        self.tree.column("one", width=80)
        self.tree.column("two", width=160)
        self.tree.column("three", width=120)
        self.tree.column("four", width=120)
        self.tree.column("five", width=80)
        self.tree.heading("one", text="Номер")
        self.tree.heading("two", text="Название")
        self.tree.heading("three", text="Единица измерения")
        self.tree.heading("four", text="Количество")
        self.tree.heading("five", text="Изменить")
        self.tree["show"] = "headings"
        self.tree.grid(row=1, column=1, columnspan=3, sticky='ew', pady=5)

    def side_bar(self):  # Боковая панель с категориями
        # Make the buttons with the icons to be shown
        btn0 = Button(self.ctr_left, text="Все", background="#896E69", foreground="#D55448", activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', highlightthickness=0, width=16)
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
                      width=16
                      )
        btn2 = Button(self.ctr_left, text="Вторые блюда", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16)
        btn3 = Button(self.ctr_left, text="Салаты", background="#896E69", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16)
        btn4 = Button(self.ctr_left, text="Закуски", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16)
        btn5 = Button(self.ctr_left, text="Десерт", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16)
        btn6 = Button(self.ctr_left, text="Напитки", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16)
        btn0.grid(row=0, column=0, pady=10)
        btn1.grid(row=1, column=0, pady=10)
        btn2.grid(row=2, column=0, pady=10)
        btn3.grid(row=3, column=0, pady=10)
        btn4.grid(row=4, column=0, pady=10)
        btn5.grid(row=5, column=0, pady=10)
        btn6.grid(row=6, column=0, pady=10)
