import tkinter as tk
from tkinter import *


class FoodCard(tk.Frame):
    def __init__(self, parent, controller,lable_text):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.lable_text=lable_text
        self.cardframe=tk.Frame(self,padx="10",pady="8",background='#FD974F',highlightbackground="#805A3B", highlightthickness=1, bd= 0)

        # canvas = Canvas(
        #     self.cardframe,
        #     width = 100, 
        #     height = 100
        #         )      
        # canvas.grid(column=0,row=0,rowspan=2)    
        self.img = tk.PhotoImage(file='assets/1234.png')  
          
        # canvas.create_image(100,100,image=self.img) 
        label1 = tk.Label(image=self.img)
        #label1.grid(column=0,row=0,rowspan=2) 
        self.plus = PhotoImage(file='assets/plus.png')
        self.minus = PhotoImage(file="assets/minus.png")
        self.size_plus = self.plus.subsample(20, 20)
        self.size_minus = self.minus.subsample(20, 20)
        label = tk.Label(self.cardframe,background='#FD974F', text=self.lable_text, font=controller.title_font)
        label.grid(column=1,row=0,rowspan=2)
        button1 = tk.Button(self.cardframe,background='#FD974F',image=self.size_plus,relief='flat', text="test", command=lambda: controller.show_frame("PageOne") )
        button2 = tk.Button(self.cardframe,background='#FD974F',image=self.size_minus,relief='flat', text="test", command=lambda: controller.show_frame("PageOne"))
        
        
        button1.grid(column=2,row=0)
        button2.grid(column=2,row=1)
       
        self.cardframe.grid(row=1,column=1)
    #     
       