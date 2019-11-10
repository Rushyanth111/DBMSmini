"""[summary]
"""
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget

from TableView import Table
from InsertDialog import InsertDialog


class InsertAndTable(QWidget):
    def __init__(self, Tablename: str, database: QSqlDatabase, parent=None):
        super().__init__(parent=parent)
        self.Tablename = Tablename
        self.database = database
        # self.FeildForm = FeildForm
        self.__set_layout__()
        # self.InsertQuery = InsertQuery

    def __set_layout__(self):
        layout = QVBoxLayout(self)

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        button = QPushButton("Input Data", self)
        button2 = QPushButton("Delete")
        button3 = QPushButton("Printer!")
        button4 = QPushButton("Test that shit!")
        button.clicked.connect(self.__insert_show__)
        button2.clicked.connect(self.__delete_row__)
        button3.clicked.connect(self.__pdf__)
        button4.clicked.connect(self.tests)
        self.table = Table(self.Tablename, self.database, self)

        layout1.addWidget(button)
        layout1.addWidget(button2)
        layout1.addWidget(button3)
        layout1.addWidget(button4)
        layout2.addWidget(self.table)
        layout.addLayout(layout1)
        layout.addLayout(layout2)

    def __insert_show__(self):
        # Form Button Holds the data even after exec_(),
        # use that incase of error
        form = InsertDialog(self.table.get_col_names(), [], [], self)

        form_result = form.exec_()
        if form_result:
            insert_result = self.table.insert_into_table(*form.get_input())

        while form_result and not insert_result:
            # form_result has to be true and insert result has to be false
            print(self.table.get_last_error())
            form_result = form.exec_()
            insert_result = self.table.insert_into_table(*form.get_input())

    def __delete_row__(self):
        self.table.__model__.removeRow(self.table.currentIndex().row())
        self.table.refresh()

    def __pdf__(self):
        pass

    def tests(self):
        print(self.table.get_col_names())
