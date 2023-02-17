import threading
from AddressPing import AddressPing
from tkinter import *
import time
from tkinter import ttk





GUI = Tk()

GUI.title("Network Check")
GUI.geometry("600x600")

style = ttk.Style()
# style.theme_use('alt')
# style.configure('TButton', background = '#0494f4', foreground = 'white', width=20, height=30,borderwidth=1, focusthickness=3, focuscolor='none')
style.map('TButton', background=[('active','red')])
style.map("Jam.TButton",
          background = [("active", "green"), ("!active", "gray")],
          foreground = [("active", "blue"), ("!active", "blue")])

style.map("Mod.TButton",
          background = [("active", "red"), ("!active", "gray")],
          foreground = [("active", "black"), ("!active", "red")])

address = Entry()
address.pack()
address.place(x=220,y=20)


x = True

addr_ping = AddressPing(GUI,address)


btn = ttk.Button(GUI,text="start ping",command=addr_ping.start_ping,style="Jam.TButton")

btn.pack()
btn.place(x=200,y=50)

btn_stop = ttk.Button(GUI,text="stop ping",command=addr_ping.stop_ping ,style="Mod.TButton") 
btn_stop.configure()
btn_stop.pack()
btn_stop.place(x=280,y=50)

addr_ping.label.place(x=100,y=100)

GUI.mainloop()