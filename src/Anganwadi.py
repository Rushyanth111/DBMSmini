"""[summary]
"""
import pathlib

from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget

from CentralDisplay import Central
from SQLinit import SQLinit

from Tabs import PTM


class Anganwadi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        layout = QVBoxLayout(self)
        tabs = self.__set_tabs__()
        layout.addWidget(tabs)

        self.setLayout(layout)

    def __set_tabs__(self):
        tabs = QTabWidget(self)

        # Initalizing SQL Database:
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName(
            pathlib.Path(__file__).parent.__str__() + "/DB/data.db"
        )
        database.open()
        SQLinit(database)

        # Tabs
        tab_person = Central("person", "name", "Text", self)

        tabs.addTab(tab_person, "PTM")
        return tabs
