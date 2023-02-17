from tkinterweb import HtmlFrame

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk



#from tkinter import *

GUI = tk.Tk()
GUI.title("WebWrapper")
GUI.geometry("800x400")


frame = HtmlFrame(GUI)

frame.load_website("http://google.co.th")
frame.pack(fill="both",expand=True)



GUI.mainloop()