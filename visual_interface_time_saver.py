# """
# Implement a GUI for viewing and updating class instances stored in a shelve;
# the shelve lives on the machine this script runs on, as 1 or more local files;
# """
import tkinter as tk
from tkinter.messagebox import showerror, askquestion
import shelve
import time_saver as ts
import time

shelvename = 'times_data/times-shelve'

fieldnames = ('name', 'months', 'time', 'pay-per-hour')
fieldnames_Date = ('name', 'date')

class Container:
    pass

class TimeSaverGUI:
    def __init__(self, db, chrono):
        self.user_name = '...'
        self.db = db
        self.chrono = chrono
        
        self.window = tk.Tk()
        self.window.title('Timer ')

        self.form = tk.Frame(self.window)
        self.form.pack()

        self.lab = tk.Label(self.form, text='Enter your name:')
        self.ent = tk.Entry(self.form)
        
        self.lab.grid(row=0, column=0)
        self.ent.grid(row=1, column=0)
        
        # self.entries['user-name'] = self.ent
        self.chrono_running = False
        self.butt_chrono = tk.Button(self.window, text="start", command=lambda : self.chrono_handler())
        self.butt_chrono.pack(side=tk.LEFT)
        
        self.butt_close = tk.Button(self.window, text="close", command=lambda : self.close())
        self.butt_close.pack(side=tk.LEFT)
        
    def mainloop(self):
        self.lab.event_generate
        self.window.mainloop()

    def chrono_handler(self):
        print(self.ent.get())
        if self.ent.get() in ('', None): 
            return
        else:
            print(self.ent.get())
            self.user_name = self.ent.get()
        
        if not self.chrono.is_running:
            self.chrono.start()
            
            self.ent.grid_remove()
            self.butt_chrono.configure(text="pause")
            self.butt_close.configure(state=tk.DISABLED)
            print('Chrono running')
        else:
            self.chrono.stop()

            self.butt_chrono.configure(text="start")
            self.butt_close.configure(state=tk.NORMAL)
            print('Chrono stoped')

    def update_timer(self):
        _time = ts.format_timedelta(self.chrono.elapsed)
        self.lab.configure(text=f'Time: {_time} \n{self.user_name}')

    def close(self):
        # save state
        self.db.close() # back here after quit or window close
        self.window.quit()



    # def updateRecord(db):
    #     key = entries['key'].get()
    #     if key in db:
    #         record = db[key]
    #         # update existing record
    #     else:
    #         # make/store new one for key
    #         record = Container()
    #         # eval: strings must be quoted
    #     for field in fieldnames:
    #         # if field == 'months': continue
    #         setattr(record, field, entries[field].get())
    #     db[key] = record

# initial_quiz = askquestion(title="?",message="You want to start the Chrono?")
db = shelve.open(shelvename)
window = TimeSaverGUI(db, ts.Chronometer(None))
window.window.mainloop()
# window.mainloop()


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
