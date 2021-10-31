from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from AutomationPO_MainWindow import Ui_MainWindow
from AboutWindow_GUI import Ui_AboutWindow
import GUILib
class MainGUI(Ui_MainWindow):
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
        PO_to_be_process = PO_information()
        PO_to_be_process = GUILib.loadPO(self)

    def loadToken(self):
        self.Token = 'not loaded'
        self.Token = GUILib.loadToken(self)

    def extractPO(self):
        GUILib.extractPO(self)

    def pushTrello(self):
        #Token = GUILib.loadToken(self)
        if self.Token != 'not loaded':
            GUILib.pushTrello(self)

class PO_information(object):
  def __init__(self):
    self.PO_filename = []
    self.PO_number = []
    self.PO_date = []
    self.PO_price = 0
    self.PO_email = []