from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget
from FormDialog import Feilds, FeildSpecify
from InsertAndTable import InsertAndTable
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
        tab_PTM = InsertAndTable(
            "PTM",
            {
                "SNo.": FeildSpecify(Feilds.Integer, True),
                "Name": FeildSpecify(Feilds.Text),
                "Guardian'sName": FeildSpecify(Feilds.Text),
                "Discussion": FeildSpecify(Feilds.Text),
            },
            db,
            """INSERT INTO PTM VALUES({},'{}','{}','{}')""",
            self,
        )

        tabs.addTab(tab_PTM, "PTM")
        return tabs
