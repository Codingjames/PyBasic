import platform
import subprocess
import tkinter as tk    

class AddressPing :
    def __init__(self,gui,ip_input) :
        self.gui = gui
        self.label = tk.Label(self.gui,text="")
        self.label.pack()
        self.count = 0
        self.loop_running = True
        self.ip_input = ip_input
    
        #self.ping()
    
    def update_label(self):
        if self.loop_running:
            self.count+=1
            text = str(self.count)+ " ping to "+ self.ip+" result is "+ self.ping(self.ip).decode('utf-8')
            self.label.config(text=text)

        self.gui.after(3000,self.update_label)


    def ping(self,host):
        if(self.ip==''):
            return
        param = '-n' if platform.system().lower() == 'windows' else '-c'

        command = ['ping',param,'1',host,]
        return subprocess.check_output(command)
    

    def start_ping(self):
        self.ip = self.ip_input.get()
        self.loop_running = True
        self.update_label()

    def stop_ping(self):
        self.loop_running = False




