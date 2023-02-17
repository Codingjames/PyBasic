import tkinter as tk

class LoopingLabel:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(self.master, text="")
        self.label.pack()
        self.count = 0
        self.loop_running = False

    def update_label(self):
        if self.loop_running:
            self.count += 1
            self.label.config(text="Count: {}".format(self.count))
        self.master.after(3000, self.update_label)

    def start_loop(self):
        self.loop_running = True
        self.update_label()

    def stop_loop(self):
        self.loop_running = False

root = tk.Tk()
label = LoopingLabel(root)

start_button = tk.Button(root, text="Start Loop", command=label.start_loop)
start_button.pack()

stop_button = tk.Button(root, text="Stop Loop", command=label.stop_loop)
stop_button.pack()

root.mainloop()