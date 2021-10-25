import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from AutomationPO_GUI import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
 def __init__(self, parent=None):
  super(MyWindow, self).__init__(parent)
  self.setupUi(self)

if __name__ == '__main__':
 app = QApplication(sys.argv)
 myWin = MyWindow()
 myWin.show()
 sys.exit(app.exec_())