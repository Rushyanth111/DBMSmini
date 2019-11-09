import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QTabWidget,
    QWidget,
)

from Anganwadi import Anganwadi


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setLayout()
        self.setTitle()
        self.setCentralWidget(CentralWidget(self))
        self.setMenu()
        self.show()

    def setLayout(self):
        posx, posy, width, height = 0, 0, 600, 600
        self.setGeometry(posx, posy, width, height)

    def setTitle(self):
        self.setWindowTitle("Anganwadi Management System")

    def setMenu(self):
        menu = self.menuBar()
        HelpMenu = menu.addMenu("Help")

        Action = QAction("Show Help", self)
        Action.triggered.connect(self.openPDF)

        HelpMenu.addAction(Action)

        self.setMenuBar(menu)

    def openPDF(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile("./Help.pdf"))


class CentralWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAllLayouts()

    def setAllLayouts(self):
        layout = QHBoxLayout(self)
        Tabs = QTabWidget(self)
        Tabs.addTab(Anganwadi(self), "Anganwadi")
        layout.addWidget(Tabs)
        self.setLayout(layout)


app = QApplication(sys.argv)
e = App()
app.exec_()
