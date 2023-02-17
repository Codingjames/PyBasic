from tkinter import ttk
class JButton:
   
   # properties
   gui_object = None
   padx = 0
   pady = 0

   def __init__(self,gui_object) :
      self.gui_object = gui_object
   
   
   def button(self,text="button_name",place_x=0,place_y=0,command=None):  
      x = ttk.Button(self.gui_object,text=text,command=command)
      x.pack()
      x.place(x=place_x,y=place_y)
