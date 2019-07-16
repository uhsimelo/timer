
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from os.path import isfile 

from core import DeltaTime, TimeSaverIO

from .mainwindow import Ui_TimerWindow
from .dialog import DialogNameChangeUI


class States:
    READY = 'Ready'
    RUNNING = 'Running'
    PAUSED = 'Paused'

class TimeSaverUI(Ui_TimerWindow):
    def __init__(self, root, name=None):
        self.setupUi(root)
        self.root = root
        self.dialog = DialogNameChangeUI(per_hour=2)
        self.root.setEnabled(False)
        self.root:QtWidgets.QMainWindow
        self.root.closeEvent = self.closeall
        self.dialog.root.closeEvent = self.setup
        self.dialog.show()

    def closeall(self, event):
        self.dialog.root.close()

    def setup(self, event=None):
        self.root.setEnabled(True)
        name, change, errors = self.dialog.dialog_result 
        if errors:
            self.root.close()
        self.time = DeltaTime()
        self.io = TimeSaverIO(name, per_hour=change)
        self.setup_vars()
        self.setup_actions()
        self.setup_lcd_times()
        self.setup_lcd_money()

    def setup_vars(self):
        self.play_icon = QtGui.QIcon()
        self.play_icon.addPixmap(QtGui.QPixmap("statics/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        
        self.pause_icon = QtGui.QIcon()
        self.pause_icon.addPixmap(QtGui.QPixmap("statics/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        
        self.timer = QtCore.QTimer(self.root)
        self.timer.setInterval(1000)

    def setup_actions(self):
        self.action_playpause.triggered.connect(self.playpause)
        self.action_stop.triggered.connect(self.stop)
        self.timer.timeout.connect(self.tick)
        self.root.closeEvent = lambda event: self.save()  

    def setup_lcd_times(self):
        self.lcdNumber_hours.setProperty('intValue', 0)
        self.lcdNumber_minutes.setProperty('intValue', 0)
        self.lcdNumber_seconds.setProperty('intValue', 0)

    def setup_lcd_money(self):
        all_month = self.io.get_money_status()
        
        self.lcdNumber_all_month.setProperty('value', all_month)
        self.lcdNumber_earning.setProperty('value', 0)

    def playpause(self):
        if not self.timer.isActive():
            self.timer.start()
            self.action_playpause.setIcon(self.pause_icon)
        else:
            self.timer.stop()
            self.action_playpause.setIcon(self.play_icon)

    def save(self):
        if self.timer.isActive():
            self.timer.stop()
        if self.time.h != 0 or self.time.m != 0:
            self.io.save_time(self.time)
        
    def stop(self):
        if self.timer.isActive():
            self.timer.stop()
        self.action_playpause.setIcon(self.play_icon)
        self.save()
        self.update_state()

    def reset(self):
        if self.timer.isActive():
            self.stop()
        self.time = DeltaTime()        
        self.setup_lcd_money()
        self.setup_lcd_times()
        self.playpause()


    def tick(self):
        self.time.s += 1
        
        self.lcdNumber_hours.setProperty('intValue', self.time.h)
        self.lcdNumber_minutes.setProperty('intValue', self.time.m)
        self.lcdNumber_seconds.setProperty('intValue', self.time.s)
        
        if self.time.h >= 100:
            self.reset()

        self.update_state()

    def update_state(self):
        if self.timer.isActive():    
            all_month, earning = self.io.get_money_status(self.time)

            self.lcdNumber_all_month.setProperty('value', all_month)
            self.lcdNumber_earning.setProperty('value', earning)
        else:                  
            self.time = DeltaTime()
            self.setup_lcd_money()
            self.setup_lcd_times()




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TimerWindow = QtWidgets.QMainWindow()
    ui = TimeSaverUI(TimerWindow)
    TimerWindow.show()
    sys.exit(app.exec_())

