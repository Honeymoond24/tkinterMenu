import tkinter as tk
from tkinter import *

from cms.header import *


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        top_frame = Frame(self, bg='cyan', pady=3)
        Header(top_frame, self.controller)
        center = Frame(self, bg='gray2', pady=3)
        btm_frame = Frame(self, bg='white', pady=3)
        btm_frame2 = Frame(self, bg='lavender', pady=3)
        # layout all of the main containers
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ns")
        center.grid(row=1, sticky="nsew")
        btm_frame.grid(row=3, sticky="ns")
        btm_frame2.grid(row=4, sticky="ns")

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        # ctr_left = Frame(center, bg='blue', width=100, height=190)
        ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
        ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)

        # ctr_left.grid(row=0, column=0, sticky="ns")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")
