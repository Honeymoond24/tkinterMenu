import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from pageMain import *
from pageOne import *
from pageTwo import *
from pageAbout import *
from menu import *
from pageCard import *


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=12, weight="bold", slant="italic")
        # self.geometry("1280x720+300+200")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        self.frames["PageMain"] = PageMain(parent=container, controller=self)
        self.frames["PageOne"] = PageOne(parent=container, controller=self)
        self.frames["PageTwo"] = PageTwo(parent=container, controller=self)
        self.frames["PageAbout"] = PageAbout(parent=container, controller=self)
        self.frames["PageCard"] = PageCard(parent=container, controller=self, link='link')

        self.frames["PageMain"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageAbout"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageCard"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageMain")
        self.menu = AppMenu(self, container)
        self.menu.add_menu()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
