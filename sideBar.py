from tkinter import *


class SideBar(Tk):
    min_w = 50 # Minimum width of the frame
    max_w = 200 # Maximum width of the frame
    cur_width = min_w # Increasing width of the frame
    expanded = False # Check if it is completely exanded

    def __init__(self, parent):
        self.sideMenu = Frame(parent)

        # menu list
        home_b = Button(self.sideMenu,
        # image=home,
        bg='orange',relief='flat')
        set_b = Button(self.sideMenu,
        # image=settings,
        bg='orange',relief='flat')
        ring_b = Button(self.sideMenu,
        # image=ring,
        bg='orange',relief='flat')
    
        self.sideMenu.pack() 

        home_b.grid(row=0,column=0,pady=10)
        set_b.grid(row=1,column=0,pady=50)
        ring_b.grid(row=2,column=0)

        self.sideMenu.bind('<Enter>',lambda e: self.expand())
        self.sideMenu.bind('<Leave>',lambda e: self.contract())
        

    def expand(self):
        self.cur_width += 10 # Increase the width by 10
        rep = self.sideMenu.after(5,self.expand) # Repeat this func every 5 ms
        self.sideMenu.config(width=self.cur_width) # Change the width to new increase width
        if self.cur_width >= self.max_w: # If width is greater than maximum width 
            self.expanded = True # Frame is expended
            self.sideMenu.after_cancel(rep) # Stop repeating the func
            self.fill()
        

    def contract(self):
        self.cur_width -= 10 # Reduce the width by 10 
        rep = self.sideMenu.after(5,self.contract) # Call this func every 5 ms
        self.sideMenu.config(width=self.cur_width) # Change the width to new reduced width
        if self.cur_width <= self.min_w: # If it is back to normal width
            self.expanded = False # Frame is not expanded
            self.sideMenu.after_cancel(rep) # Stop repeating the func
            self.fill()

    def fill(self):
        if self.expanded: # If the frame is exanded
            # Show a text, and remove the image
            self.home_b.config(text='Home',image='',font=(0,21))
            self.set_b.config(text='Settings',image='',font=(0,21))
            self.ring_b.config(text='Bell Icon',image='',font=(0,21))
        else:
            # Bring the image back
            self.home_b.config(font=(0,21))
            self.set_b.config(font=(0,21))
            self.ring_b.config(font=(0,21))

