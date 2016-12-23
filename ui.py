# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(290, 323)
        Form.setMinimumSize(QtCore.QSize(290, 323))
        Form.setMaximumSize(QtCore.QSize(290, 323))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_lab = QtGui.QPushButton(Form)
        self.pushButton_lab.setGeometry(QtCore.QRect(10, 80, 131, 41))
        self.pushButton_lab.setObjectName(_fromUtf8("pushButton_lab"))
        self.pushButton_start = QtGui.QPushButton(Form)
        self.pushButton_start.setGeometry(QtCore.QRect(150, 80, 131, 41))
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 120, 271, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_start, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.clicked_start)
        QtCore.QObject.connect(self.pushButton_lab, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.clicked_lab)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "StopWatch", None))
        self.lineEdit.setText(_translate("Form", "00:00:00.00", None))
        self.pushButton_lab.setText(_translate("Form", "Lab", None))
        self.pushButton_start.setText(_translate("Form", "Start", None))

