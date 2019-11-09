"""[summary]
"""
import string

import openpyxl
from pandas import DataFrame

from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget

from FormDialog import FormDialog
from TableView import Table


class InsertAndTable(QWidget):
    def __init__(
        self,
        Tablename: str,
        FeildForm: dict,
        database: QSqlDatabase,
        InsertQuery: str,
        parent=None,
    ):
        super().__init__(parent=parent)
        self.Tablename = Tablename
        self.database = database
        self.FeildForm = FeildForm
        self.setInsertAndLayout()
        self.InsertQuery = InsertQuery

    def setInsertAndLayout(self):
        layout = QVBoxLayout(self)

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        button = QPushButton("Input Data", self)
        button2 = QPushButton("Delete")
        button3 = QPushButton("Printer!")

        button.clicked.connect(self.InsertShow)
        button2.clicked.connect(self.DeleteRow)
        button3.clicked.connect(self.pdf)
        self.table = Table(self.Tablename, self.database, self)

        layout1.addWidget(button)
        layout1.addWidget(button2)
        layout1.addWidget(button3)
        layout2.addWidget(self.table)
        layout.addLayout(layout1)
        layout.addLayout(layout2)

    def InsertShow(self):
        FormButton = FormDialog(self.Tablename, self.FeildForm, self)
        result = FormButton.exec_()
        print(result)
        if result == 1:
            print("Called Insert")
            self.table.insert_into_table(*FormButton.GetAllFeildResponses())

    def DeleteRow(self):
        self.table.__model__.removeRow(self.table.currentIndex().row())
        self.table.refresh()

    def pdf(self):
        print("Not Yet Implemented.")
