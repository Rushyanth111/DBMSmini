import sys

from PyQt5.QtCore import QUrl, pyqtSlot
from PyQt5.QtGui import QDesktopServices, QIcon
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtSql import QSqlDatabase
from Anganwadi import Anganwadi
from School import School

from SQLinit import SQLinit


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
        self.setWindowTitle("DBMS Mini Project")

    def setMenu(self):
        menu = self.menuBar()
        HelpMenu = menu.addMenu("Help")

        Action = QAction("HELP", self)
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

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("projects.db")
        db.open()
        SQLinit(db)
        Tabs.addTab(Anganwadi(db, self), "Anganwadi")
        Tabs.addTab(School(db, self), "School")
        layout.addWidget(Tabs)
        self.setLayout(layout)


app = QApplication(sys.argv)
e = App()
app.exec_()
