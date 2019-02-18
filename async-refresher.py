import tkinter as tk
import time

def Draw():
    global label_time

    frame=tk.Frame(root,width=100,height=100,relief='solid',bd=1)
    frame.place(x=10,y=10)
    label_time=tk.Label(frame,text='HELLO')
    label_time.pack()

def Refresher():
    global label_time
    label_time.configure(text=time.asctime())
    root.after(1000, Refresher) # every second...

root=tk.Tk()
Draw()
Refresher()
root.mainloop()
