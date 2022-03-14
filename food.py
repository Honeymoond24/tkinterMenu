from tkinter import *
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
        self.ctr_right = Frame(center, bg='#FEF2E4', padx=3, pady=3)

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.side_bar()
        self.ctr_right.grid(row=0, column=1, sticky="ns")
        top_frame.grid(row=0, sticky="EW")
        center.grid(row=1, column=0, sticky="nsew")
        self.cards0 = FoodCard(self.ctr_right, self.controller, "Мука")
        self.cards1 = FoodCard(self.ctr_right, self.controller, "Картофель")
        self.cards2 = FoodCard(self.ctr_right, self.controller, "Морковь")
        self.cards3 = FoodCard(self.ctr_right, self.controller, "Гречневая крупа")
        self.cards4 = FoodCard(self.ctr_right, self.controller, "Рис")
        self.cards5 = FoodCard(self.ctr_right, self.controller, "Лук")
        self.cards6 = FoodCard(self.ctr_right, self.controller, "Горох")
        self.cards7 = FoodCard(self.ctr_right, self.controller, "Сельдерей")
        self.cards0.grid(row=1, column=0)
        self.cards1.grid(row=1, column=1)
        self.cards2.grid(row=1, column=2)
        self.cards3.grid(row=1, column=3)
        self.cards4.grid(row=2, column=0)
        self.cards5.grid(row=2, column=1)
        self.cards6.grid(row=2, column=2)
        self.cards7.grid(row=2, column=3)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)

        # layout all of the main containers
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=10)

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
