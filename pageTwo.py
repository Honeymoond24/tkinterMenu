import tkinter as tk
from tkinter import *
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        

        top_frame = Frame(self, bg='cyan', width=450, height=50, pady=3)
        center = Frame(self, bg='gray2', width=50, height=40, padx=3, pady=3)
        btm_frame = Frame(self, bg='white', width=450, height=45, pady=3)
        btm_frame2 = Frame(self, bg='lavender', width=450, height=60, pady=3)

        # label = tk.Label(top_frame, text="This is the start page1", font=controller.title_font)
        button1 = tk.Button(top_frame, text="Go to Page One", command=lambda: controller.show_frame("PageMain"))
        button2 = tk.Button(top_frame, text="Go to Page Two", command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(top_frame, text="About", command=lambda: controller.show_frame("PageAbout"))
        # layout all of the main containers
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")
        btm_frame.grid(row=3, sticky="ew")
        btm_frame2.grid(row=4, sticky="ew")

        # label.grid(row=0, column=0,  sticky="nsew")
        button1.grid(row=0, column=1,  sticky="nsew")
        button2.grid(row=0, column=2,  sticky="nsew")
        button3.grid(row=0, column=3,  sticky="nsew")

        #

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        # ctr_left = Frame(center, bg='blue', width=100, height=190)
        ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
        ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)

        # ctr_left.grid(row=0, column=0, sticky="ns")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")

