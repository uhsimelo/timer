from PyQt5 import QtWidgets,QtGui

from .dialogname import Ui_DialogName
from .utils import DoubleValidator

from config import PATH_FILES
from core import get_names

class DialogNameChangeUI(Ui_DialogName):
    def __init__(self, default_name="", per_hour=1):
        self.root = QtWidgets.QWidget()
        self.setupUi(self.root)
        self.root.setFocus(True)
        names = get_names(PATH_FILES)
        default_name = names[0] if names else default_name 
        self.dialog_result = (default_name, per_hour, 1)
        self.lineEdit_change.setValidator(DoubleValidator())
        self.lineEdit_change.setText(str(per_hour))
        self.lineEdit_name.setText(str(default_name))

        self.pushButton_accept.clicked.connect(self.accept)
    
    def show(self):
        self.root.show()
        self.root.setFocus() # FIXME: Make it work 

    def accept(self, event=None):
        if len(self.lineEdit_name.text()) == 0 or len(self.lineEdit_change.text()) <= 0 or float(self.lineEdit_change.text()) <= 0:
            self.dialog_result = *self.dialog_result[:2], 1
            return
 
        self.dialog_result = self.lineEdit_name.text(), float(self.lineEdit_change.text()), 0
        self.root.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = DialogNameChangeUI(default_name="", per_hour=12)
    ui.show()
    sys.exit(app.exec_())

