from tkinter import *
from tkinter import ttk # Theme
from tkinter import messagebox
GUI = Tk()

#Set Application attribute
GUI.title("โปรแกรมบันทึกข้อมูล")
GUI.geometry("800x600")

#Label
L1 = Label(GUI,text="Label1",font=('Angsana New',30),fg='green')
L1.place(x=100,y=30)

FB = Frame(GUI)
FB.place(x=200,y=500)

B1 = Button(FB,text="บันทึกข้อมูล")
B1.pack(ipadx=20,ipady=20)

# This function
def Button2():
    text = 'Show somthings'
    #messagebox.showinfo("Message show : ",text)
    messagebox.showerror("Message show : ",text)
    #messagebox.showwarning("Message show : ",text)

    
B2 = ttk.Button(GUI,text="ปุ่ม 2",command=Button2)
B2.pack()
B2.place(x=200,y=300)







GUI.mainloop()
