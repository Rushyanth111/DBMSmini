import sys
import pathlib

from PyQt5.QtCore import QUrl, Qt, QFile
from PyQt5.QtGui import QDesktopServices, QFont 
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QVBoxLayout,
    QMainWindow,
    QTabWidget,
    QWidget,
    QLabel,
)

import qdarkstyle
import qtmodern.styles
import qtmodern.windows
from Anganwadi import Anganwadi
from Login import QLogin

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
        layout = QVBoxLayout(self)

        X = QLabel("<i><u>Anganwadi</u> Database<br>Management System</i><br>", self)
        X.setStyleSheet("font-size:14pt; color: White; font: Verdana;")
        X.setTextFormat(Qt.RichText)
        X.setAlignment(Qt.AlignHCenter)
        X.setFont(QFont("Segoe UI", 14))

        layout.addWidget(X)
        layout.addWidget(Anganwadi(self))
        self.setLayout(layout)


APP = QApplication(sys.argv)

#APP.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
#LOGIN = QLogin()
#if LOGIN.exec():
MAIN = App()


qtmodern.styles.dark(APP)
mw = qtmodern.windows.ModernWindow(MAIN)
mw.show()

APP.exec_()