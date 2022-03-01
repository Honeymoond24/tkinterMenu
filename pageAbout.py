import tkinter as tk
from tkinter import font as tkfont


class PageAbout(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self,
                          text="Данная программа была разработана \nв рамках лабораторной работы 2.\n\n"
                               "Работу выполнили студенты группы АПО-19:\n"
                               "Жантурин Д.Р.\n"
                               "Семейников А.Н.\n"
                               "Долгушин Н.Л.\n"
                               "Одарич К.Н.",
                          font=tkfont.Font(family='Helvetica', size=12,
                                           # weight="bold",
                                           slant="italic"))
        label1.grid(row=1, column=1)
        button = tk.Button(self, text="Вернуться на главную страницу",
                           command=lambda: controller.show_frame("PageMain"),
                           background="#D55448",  # фоновый цвет кнопки
                           foreground="#F9F9FF",  # цвет текста
                           padx="20",  # отступ от границ до содержимого по горизонтали
                           pady="8",  # отступ от границ до содержимого по вертикали
                           font="16",  # высота шрифта
                           )
        button.grid(row=2, column=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=10)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=1)
