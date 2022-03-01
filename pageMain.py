import tkinter as tk
from tkinter import *

class PageMain(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        top_frame = Frame(self, bg='cyan', pady=3)
        center = Frame(self, bg='gray2', pady=3)
        btm_frame = Frame(self, bg='white', pady=3)
        btm_frame2 = Frame(self, bg='lavender', pady=3)

        label = tk.Label(top_frame, text="MainPage", font=controller.title_font)
        button1 = tk.Button(top_frame, text="Go to Page Main", command=lambda: controller.show_frame("PageMain"))
        button2 = tk.Button(top_frame, text="Go to Page One", command=lambda: controller.show_frame("PageOne"))
        button3 = tk.Button(top_frame, text="Go to Page Two", command=lambda: controller.show_frame("PageTwo"))
        button4 = tk.Button(top_frame, text="About", command=lambda: controller.show_frame("PageAbout"))
        # layout all of the main containers
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")
        btm_frame.grid(row=3, sticky="ew")
        btm_frame2.grid(row=4, sticky="ew")

        label.grid(row=0, column=0,  sticky="nsew")
        button1.grid(row=0, column=1,  sticky="nsew")
        button2.grid(row=0, column=2,  sticky="nsew")
        button3.grid(row=0, column=3,  sticky="nsew")
        button4.grid(row=0, column=4,  sticky="nsew")

        # create the widgets for the top frame
        # model_label = Label(top_frame, text='Model Dimensions')
        # width_label = Label(top_frame, text='Width:')
        # length_label = Label(top_frame, text='Length:')
        # entry_W = Entry(top_frame, background="pink")
        # entry_L = Entry(top_frame, background="orange")

        # layout the widgets in the top frame
        # model_label.grid(row=0, columnspan=3)
        # width_label.grid(row=1, column=0)
        # length_label.grid(row=1, column=2)
        # entry_W.grid(row=1, column=1)
        # entry_L.grid(row=1, column=3)

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        ctr_left = Frame(center, bg='blue')
        ctr_mid = Frame(center, bg='yellow', padx=3, pady=3)
        ctr_right = Frame(center, bg='green', padx=3, pady=3)

        ctr_left.grid(row=0, column=0, sticky="ns")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")
