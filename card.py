import tkinter as tk
from tkinter import *
from pageCard import *


class Card(tk.Frame):
    def __init__(self, parent, controller, lable_text, link):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.lable_text=lable_text
        self.link = link
        self.cardframe=tk.Frame(self,padx="10",pady="8",background='#FD974F',highlightbackground="#805A3B", highlightthickness=1, bd= 0)

        canvas = Canvas(
            self.cardframe,
            width = 100, 
            height = 100
                )      
        canvas.grid(column=0,row=0,rowspan=2)    
        img = tk.PhotoImage(master=canvas,file='assets/1234.png')  
          
        canvas.create_image(
            100,
            100, 
            anchor=NW, 
            image=img
            )


        label = tk.Label(self.cardframe,background='#FFA577',foreground= "#896E69", text=self.lable_text, font=controller.title_font)
        label.grid(column=1,row=0)
        # self.controller.frames[self.link] = PageCard(parent=self, controller=controller, link=self.link)
        button1 = tk.Button(self.cardframe, text="test", command=lambda: controller.show_frame('PageCard'),
                             background="#555",  # фоновый цвет кнопки
                             foreground="#ccc",  # цвет текста
                             padx="20",  # отступ от границ до содержимого по горизонтали
                             pady="8",  # отступ от границ до содержимого по вертикали
                             font="5"  # высота шрифта
                             )
        button1.grid(column=1,row=1)
       
        self.cardframe.grid(row=1,column=1)
