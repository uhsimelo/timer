"""
Implement a GUI for viewing and updating class instances stored in a shelve;
the shelve lives on the machine this script runs on, as 1 or more local files;
"""
import tkinter as tk
from tkinter.messagebox import showerror, askquestion
import shelve

shelvename = 'times_data/times-shelve'

fieldnames = ('name', 'months', 'time', 'pay-per-hour')
fieldnames_Date = ('name', 'date')

class Container:
    pass

def makeWidgets():
    global entries
    window = tk.Tk()
    window.title('Timer')
    form = tk.Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',) + fieldnames):
        # if label == 'months': continue
        lab = tk.Label(form, text=label)
        ent = tk.Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    tk.Button(window, text="Fetch", command=lambda : fetchRecord(db)).pack(side=tk.LEFT)
    tk.Button(window, text="Update", command=lambda : updateRecord(db)).pack(side=tk.LEFT)
    tk.Button(window, text="Quit", command=lambda : close(db)).pack(side=tk.RIGHT)
    return window

def fetchRecord(db):
    key = entries['key'].get()
    try:
        record = db[key]
        # fetch by key, show in GUI
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, tk.END)
            entries[field].insert(0, repr(getattr(record, field)))

def updateRecord(db):
    key = entries['key'].get()
    if key in db:
        record = db[key]
        # update existing record
    else:
        # make/store new one for key
        record = Container()
        # eval: strings must be quoted
    for field in fieldnames:
        # if field == 'months': continue
        setattr(record, field, entries[field].get())
    db[key] = record

def close(db):
    db.close() # back here after quit or window close
    window.quit()

# initial_quiz = askquestion(title="?",message="You want to start the Chrono?")
db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()


# # from tkinter import *
# # import random
# # fontsize = 30
# # colors = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'purple']
# # def onSpam():
# #     popup = Toplevel()
# #     color = random.choice(colors)
# #     Label(popup, text='Popup', bg='black', fg=color).pack(fill=BOTH)
# #     mainLabel.config(fg=color)
# # def onFlip():
# #     mainLabel.config(fg=random.choice(colors))
# #     main.after(250, onFlip)
# # def onGrow():
# #     global fontsize
# #     fontsize += 5
# #     mainLabel.config(font=('arial', fontsize, 'italic'))
# #     main.after(100, onGrow)

# # main = Tk()
# # mainLabel = Label(main, text='Fun Gui!', relief=RAISED)
# # mainLabel.config(font=('arial', fontsize, 'italic'), fg='cyan',bg='navy')
# # mainLabel.pack(side=TOP, expand=YES, fill=BOTH)
# # Button(main, text='spam', command=onSpam).pack(fill=X)
# # Button(main, text='flip', command=onFlip).pack(fill=X)
# # Button(main, text='grow', command=onGrow).pack(fill=X)
# # main.mainloop()
