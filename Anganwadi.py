from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget

from CentralTable import Central
from InsertDialog import InsertDialog
from SQLinit import SQLinit


class Anganwadi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setInternalCategory()

    def setInternalCategory(self):
        layout = QVBoxLayout(self)
        tabs = self.makeInternalTabs()
        layout.addWidget(tabs)

        self.setLayout(layout)

    def makeInternalTabs(self):
        tabs = QTabWidget(self)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("projects.db")
        db.open()
        SQLinit(db)
        tab_PTM = Central("PTM", self)

        tab_S = Central("Admission", self)

        tabs.addTab(tab_PTM, "PTM")
        tabs.addTab(tab_S, "S")
        return tabs
