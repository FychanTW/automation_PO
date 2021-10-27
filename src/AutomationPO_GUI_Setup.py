from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from AutomationPO_MainWindow import Ui_MainWindow
from AboutWindow_GUI import Ui_AboutWindow
import GUILib
class MainGUI(Ui_MainWindow):
    print("new class")
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.actionAbout.triggered.connect(self.openAboutWindow)
        self.model = QtCore.QStringListModel()
        self.PONum_model = QtCore.QStringListModel()
        self.LoadPOBtn.clicked.connect(self.loadPO)
        self.LoadTokenBtn.clicked.connect(self.loadToken)
        self.pushTrelloBtn.clicked.connect(self.pushTrello)

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)

    def openAboutWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def loadPO(self):
        GUILib.loadPO(self)

    def loadToken(self):
        Token = GUILib.loadToken(self)

    def extractPO(self):
        GUILib.extractPO(self)

    def pushTrello(self,Token):
        GUILib.pushTrello(self,Token)