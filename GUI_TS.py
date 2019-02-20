import tkinter as tk
import time_saver as ts

class Container:
    pass

class TimeSaverGUI:
    def __init__(self, chrono):
        self.user_name = None
        self.db = None
        self.chrono = chrono
        
        self.master = tk.Tk()
        self.master.title('Timer ')

        self.form = tk.Frame(self.master)
        self.form.pack()

        self.lab_main = tk.Label(self.form, text='Enter your name:')
        self.lab = tk.Label(self.form, text='')
        self.ent = tk.Entry(self.form)

        self.lab_main.grid(row=0, column=0)
        self.lab.grid(row=1)
        self.ent.grid(row=2, column=0)
        
        # self.entries['user-name'] = self.ent
        self.butt_chrono = tk.Button(self.master, text="start", command=lambda : self.chrono_handler())
        self.butt_chrono.pack(side=tk.LEFT)
        
        self.butt_close = tk.Button(self.master, text="close", command=self.master.quit)
        self.butt_close.pack(side=tk.LEFT)
        
    def mainloop(self):
        self.refresher()
        self.master.mainloop()
        self.close()

    def refresher(self):
        if self.user_name not in (None, ''):
            self.update_timer()
        self.master.after(1000, func=self.refresher)

    def chrono_handler(self):
        self.user_name = self.user_name if self.user_name not in (None, '') else self.ent.get()
        
        if self.user_name in (None, ''):
            return 

        if not self.chrono.is_running:
            self.chrono.start()

            self.ent.grid_remove()
            self.lab_main.grid_remove()

            self.butt_chrono.configure(text="pause")
            self.butt_close.configure(state=tk.DISABLED)
            print('Chrono running')
        else:
            self.chrono.stop()

            self.butt_chrono.configure(text="start")
            self.butt_close.configure(state=tk.NORMAL)
            self.save_time()
            print('Chrono stoped')

    def update_timer(self):
        _time = ts.format_timedelta(self.chrono.elapsed)
        self.lab.configure(text=f'Time: {_time} \nUser-Id: {self.user_name}')

    def save_time(self):
        # print(self.user_name)
        if self.chrono.elapsed.seconds // 60 > 0: 
            ts.save_time(self.user_name, self.chrono.cur_start, self.chrono.elapsed)

    def close(self):
        # save state
        print("Closing...")
        if self.chrono.is_running and self.chrono.elapsed.seconds > 60:
            self.save_time()
            self.elapsed = ts.timedelta(0)
        self.master.quit()


master = TimeSaverGUI(ts.Chronometer(None))
master.mainloop()
