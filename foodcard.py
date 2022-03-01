import tkinter as tk
from tkinter import *


class FoodCard(tk.Frame):
    def __init__(self, parent, controller, label_text):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.c = 0
        self.controller = controller
        self.label_text = label_text
        self.card_frame = tk.Frame(self, padx="10", pady="8", background='#FD974F', highlightbackground="#805A3B",
                                   highlightthickness=1, bd=0, width=16)

        # canvas = Canvas(
        #     self.card_frame,
        #     width = 100, 
        #     height = 100
        #         )      
        # canvas.grid(column=0,row=0,rowspan=2)     
        # canvas.create_image(100,100,image=self.img) 

        self.plus = PhotoImage(file='assets/plus.png')
        self.minus = PhotoImage(file="assets/minus.png")
        self.size_plus = self.plus.subsample(20, 20)
        self.size_minus = self.minus.subsample(20, 20)

        label = tk.Label(self.card_frame, background='#FD974F', text=self.label_text, font=controller.title_font)
        label.grid(column=1, row=0, rowspan=2)

        self.label_count = Label(self.card_frame, text="0", background='#FD974F', font=controller.title_font)
        self.label_count.grid(column=3, row=0, rowspan=2)

        button1 = tk.Button(self.card_frame, background='#FD974F', activebackground="#FFA577", image=self.size_plus,
                            relief='flat', text="test", command=lambda: self.click_button('1'))
        button2 = tk.Button(self.card_frame, background='#FD974F', activebackground="#FFA577", image=self.size_minus,
                            relief='flat', text="test", command=lambda: self.click_button('2'))

        button1.grid(column=2, row=0)
        button2.grid(column=2, row=1)

        self.card_frame.grid(row=0, column=0)
        self.card_frame.grid_rowconfigure(0, weight=10)
        self.card_frame.grid_columnconfigure(0, weight=1)

    def click_button(self, text):
        if text == "1":
            self.c += 1
            self.label_count.config(text=self.c)
        elif text == "2" and self.c != 0:
            self.c -= 1
            self.label_count.config(text=self.c)
