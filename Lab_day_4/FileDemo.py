from tkinter import *
from tkinter import ttk


GUI = Tk()
GUI.geometry("600x600")
GUI.title("Files Demo")

label_list = ttk.Label(GUI,background="lightblue",padding=2)
label_list.pack()


some_file = 'test.txt'

# write files
with open(some_file,'a',encoding='utf-8') as file :
    file.writelines('www.chiangrai-it.com \n')
    


with open(some_file,'r') as file_obj:
    lines = file_obj.readlines()

text_list = ""

for line in lines:
    
    text_list+= line
    

label_list.config(text=text_list)




GUI.mainloop()