# -*- encoding:utf8 -*-
import os,sys,time,datetime
from PyQt4 import QtCore,QtGui
from ui import *
from tendo import singleton #중복실행 방지

class MyForm(QtGui.QMainWindow):
    def closeEvent(self, event):
        sys.exit(0)

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #TaskThread
        self.taskthread = TaskThread()
        self.taskthread.lineEdit.connect(self.ui.lineEdit.setText)
        self.taskthread.start()

        self.ui.pushButton_lab.setDisabled(True)
        self.ui.listWidget.dragDropMode()
        self.labnum = 1

    def clicked_start(self):
        self.ui.pushButton_lab.setDisabled(False)
        if self.taskthread.running:#Stop
            self.taskthread.running = False
            self.ui.pushButton_start.setText('Start'.decode('utf8'))
            self.ui.pushButton_lab.setText('Reset'.decode('utf8'))
        else:#Start
            self.taskthread.running = True
            self.ui.pushButton_start.setText('Stop'.decode('utf8'))
            self.ui.pushButton_lab.setText('Lab'.decode('utf8'))
    def clicked_lab(self):
        if self.taskthread.running:#Lab
            self.ui.listWidget.insertItem(0,'Lab'.decode('utf8') + str(self.labnum)+' ' + self.taskthread.convert(self.taskthread.times))
            self.labnum += 1
        else:#Reset
            self.taskthread.times = 0.0
            self.ui.lineEdit.setText('00:00:00.00')
            self.labnum = 1
            for i in reversed(range(self.ui.listWidget.count())):
                self.ui.listWidget.takeItem(i)
            self.ui.pushButton_lab.setText('Lab'.decode('utf8'))
            self.ui.pushButton_lab.setDisabled(True)

class TaskThread(QtCore.QThread):
    lineEdit = QtCore.pyqtSignal(str)
    running = False
    times = 0.0
    def run(self):
        while True:
            if self.running:
                self.times += 0.01
                self.lineEdit.emit(self.convert(self.times))
            time.sleep(0.01)
    def convert(self,times):
        Second,MicroSecond = str(times).split('.')
        Hours = str((int(Second) / 60) / 60).zfill(2)
        Minutes = str((int(Second) / 60) % 60).zfill(2)
        Seconds = str(int(Second) % 60).zfill(2)
        MicroSeconds = MicroSecond.ljust(2, '0')
        return '%s:%s:%s.%s'%(Hours,Minutes,Seconds,MicroSeconds)

if __name__ == '__main__':
    try:
        approot = os.path.dirname(os.path.abspath(__file__))
    except NameError:  # We are the main py2exe script, not a module
        approot = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(approot)

    me = singleton.SingleInstance()
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())