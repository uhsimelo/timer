# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'askname.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogName(object):
    def setupUi(self, DialogName):
        DialogName.setObjectName("DialogName")
        DialogName.resize(318, 120)
        DialogName.setMinimumSize(QtCore.QSize(318, 120))
        DialogName.setMaximumSize(QtCore.QSize(318, 120))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        DialogName.setFont(font)
        DialogName.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("statics/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogName.setWindowIcon(icon)
        self.groupBox_name = QtWidgets.QGroupBox(DialogName)
        self.groupBox_name.setGeometry(QtCore.QRect(10, 0, 201, 71))
        self.groupBox_name.setObjectName("groupBox_name")
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox_name)
        self.lineEdit_name.setGeometry(QtCore.QRect(10, 30, 181, 25))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.groupBox_change = QtWidgets.QGroupBox(DialogName)
        self.groupBox_change.setGeometry(QtCore.QRect(220, 0, 91, 71))
        self.groupBox_change.setObjectName("groupBox_change")
        self.lineEdit_change = QtWidgets.QLineEdit(self.groupBox_change)
        self.lineEdit_change.setGeometry(QtCore.QRect(20, 30, 51, 25))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_change.setFont(font)
        self.lineEdit_change.setText("")
        self.lineEdit_change.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_change.setPlaceholderText("")
        self.lineEdit_change.setClearButtonEnabled(False)
        self.lineEdit_change.setObjectName("lineEdit_change")
        self.pushButton_accept = QtWidgets.QPushButton(DialogName)
        self.pushButton_accept.setGeometry(QtCore.QRect(110, 80, 80, 25))
        self.pushButton_accept.setObjectName("pushButton_accept")

        self.retranslateUi(DialogName)
        QtCore.QMetaObject.connectSlotsByName(DialogName)

    def retranslateUi(self, DialogName):
        _translate = QtCore.QCoreApplication.translate
        DialogName.setWindowTitle(_translate("DialogName", "Who are you, and what is your pay?"))
        self.groupBox_name.setTitle(_translate("DialogName", "Name (id)"))
        self.groupBox_change.setTitle(_translate("DialogName", "Change ($/h)"))
        self.pushButton_accept.setText(_translate("DialogName", "Accept"))
        self.pushButton_accept.setShortcut(_translate("DialogName", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogName = QtWidgets.QWidget()
    ui = Ui_DialogName()
    ui.setupUi(DialogName)
    DialogName.show()
    sys.exit(app.exec_())

