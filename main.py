import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QWidget,
    QAction,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLayout,
    QMenuBar
)
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtCore import pyqtSlot, QUrl
from Anganwadi import Anganwadi

from School import School
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setLayout()
        self.setTitle()
        self.setCentralWidget(CentralWidget(self))
        self.setMenu();
        self.show()

    def setLayout(self):
        posx, posy, width, height = 0, 0, 600, 600
        self.setGeometry(posx, posy, width, height)

    def setTitle(self):
        self.setWindowTitle("Marsandra Anganwadi Database Management System")

    def setMenu(self):
        menu = self.menuBar()
        HelpMenu = menu.addMenu("Help");
        
        Action = QAction("HELP",self);
        Action.triggered.connect(self.openPDF)
        
        HelpMenu.addAction(Action)
        
        self.setMenuBar(menu);

    def openPDF(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile("./Help.pdf"))

class CentralWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAllLayouts()

    def setAllLayouts(self):
        layout = QHBoxLayout();

        layout.addWidget(Anganwadi(self)); 
        self.setLayout(layout)


app = QApplication(sys.argv)
e = App()
app.exec_()