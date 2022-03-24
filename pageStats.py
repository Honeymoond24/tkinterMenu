from tkinter import *
from card import *
from header import *
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PageStats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent  # Родительский элемент
        self.controller = controller  # это кто?
        # Фреймы, верстка
        self.top_frame = Frame(self)
        Header(self.top_frame, self.controller)
        self.center = Frame(self)

        # layout all of the main containers
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        self.top_frame.grid(row=0, sticky="ew")
        self.center.grid(row=1, sticky="nsew")

        # create the center widgets
        self.center.grid_rowconfigure(0, weight=1)
        self.center.grid_columnconfigure(1, weight=1)

        self.ctr_left = Frame(self.center, bg='#00bff6')
        self.frames = {"stats_frame1": Frame(self.center),
                       "stats_frame2": Frame(self.center),
                       "stats_frame3": Frame(self.center),
                       "stats_frame4": Frame(self.center)}

        self.ctr_left.grid(row=0, column=0, sticky="ns")
        self.side_bar()
        # Переменные для боковой панели
        self.frames["stats_frame1"].grid(row=0, column=1, sticky="nsew")
        self.frames["stats_frame2"].grid(row=0, column=1, sticky="ns")
        self.frames["stats_frame3"].grid(row=0, column=1, sticky="ew")
        self.frames["stats_frame4"].grid(row=0, column=1, sticky="nsew")

        # Статистика 1
        self.canvas1 = tk.Canvas(self.frames["stats_frame1"], bg='black')
        self.stockListExp = ['AMZN', 'AAPL', 'JETS', 'CCL', 'NCLH']
        self.stockSplitExp = [15, 25, 40, 10, 10]
        self.fig1 = Figure()  # create a figure object
        self.ax1 = self.fig1.add_subplot(111)  # add an Axes to the figure
        self.ax1.pie(self.stockSplitExp, radius=1, labels=self.stockListExp, autopct='%0.2f%%', shadow=True, )
        self.chart1 = FigureCanvasTkAgg(self.fig1, self.canvas1)
        self.chart1.get_tk_widget().pack()
        self.canvas1.pack()

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
                      width=16,
                      command=lambda: self.show_frame("stats_frame1")
                      )
        btn2 = Button(self.ctr_left, text="Блюда чаще всего\nв меню", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      command=lambda: self.show_frame("stats_frame2"),
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16)
        btn3 = Button(self.ctr_left, text="Самые затрачиваемые\nпродукты", background="#896E69", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      command=lambda: self.show_frame("stats_frame3"),
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16)
        btn4 = Button(self.ctr_left, text="Самые популярные\nблюда", background="#00bff6", foreground="#F9F9FF",
                      activebackground="#00bff6",
                      command=lambda: self.show_frame("stats_frame4"),
                      padx="20", pady="8", font="16", bg='#00bff6', relief='flat', width=16)
        btn1.grid(row=0, column=0, pady=10)
        btn2.grid(row=1, column=0, pady=10)
        btn3.grid(row=2, column=0, pady=10)
        btn4.grid(row=3, column=0, pady=10)

    def show_frame(self, page_name):
        self.frame = self.frames[page_name]
        self.frame.tkraise()
