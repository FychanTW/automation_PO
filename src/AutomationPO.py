import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from AutomationPO_MainWindow import Ui_MainWindow
from AutomationPO_GUI_Setup import MainGUI

#class MyWindow(QMainWindow, Ui_MainWindow):
class MyWindow(QMainWindow, MainGUI):
 def __init__(self, parent=None):
  super(MyWindow, self).__init__(parent)
  self.setupUi(self)

if __name__ == '__main__':
 app = QApplication(sys.argv)
 myWin = MyWindow()
 myWin.show()
 sys.exit(app.exec_())