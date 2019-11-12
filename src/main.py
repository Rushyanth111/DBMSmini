import sys
import pathlib

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

        posx, posy, width, height = 0, 0, 600, 600
        self.setGeometry(posx, posy, width, height)

        self.setWindowTitle("Anganwadi Management System")

        self.setCentralWidget(CentralWidget(self))
        self.__set_menu__()

        self.show()

    def __set_menu__(self):
        menu = self.menuBar()
        help_menu = menu.addMenu("Help")

        pdf_open_action = lambda: QDesktopServices.openUrl(
            QUrl.fromLocalFile(str(pathlib.Path(__file__).parent) + "/docs/Help.pdf")
        )
        action = QAction("Show Help", self)
        action.triggered.connect(pdf_open_action)

        help_menu.addAction(action)

        self.setMenuBar(menu)


class CentralWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        tabs = QTabWidget(self)
        tabs.addTab(Anganwadi(self), "Anganwadi")
        layout.addWidget(tabs)
        self.setLayout(layout)


app = QApplication(sys.argv)
e = App()
app.exec_()
