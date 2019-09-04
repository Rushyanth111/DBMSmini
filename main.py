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
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from Anganwadi import Anganwadi

from School import School
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setLayout()
        self.setTitle()
        self.setCentralWidget(CentralWidget(self))
        self.show()

    def setLayout(self):
        posx, posy, width, height = 0, 0, 600, 600
        self.setGeometry(posx, posy, width, height)

    def setTitle(self):
        self.setWindowTitle("DBMS Mini Project")


class CentralWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAllLayouts()

    def setAllLayouts(self):
        layout = QVBoxLayout(self)
        tabs = self.makeTabs()

        layout.addWidget(tabs)
        self.setLayout(layout)

    def makeTabs(self):
        tabs = QTabWidget(self)

        tab1 = Anganwadi(self)
        tab2 = School(self)
        tabs.addTab(tab1, "Anganwadi")
        tabs.addTab(tab2, "School")

        return tabs


app = QApplication(sys.argv)
e = App()
app.exec_()