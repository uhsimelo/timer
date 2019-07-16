from gui import TimeSaverUI
from PyQt5 import QtWidgets


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TimerWindow = QtWidgets.QMainWindow()
    ui = TimeSaverUI(TimerWindow)
    TimerWindow.show()
    sys.exit(app.exec_())

