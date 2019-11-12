"""[summary]
"""
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QMessageBox,
    QDialogButtonBox,
)

from TableView import Table
from InsertDialog import InsertDialog


class Central(QWidget):
    def __init__(self, Tablename: str, parent=None):
        super().__init__(parent=parent)
        self.Tablename = Tablename
        self.database = QSqlDatabase()
        # self.FeildForm = FeildForm
        self.__set_layout__()
        # self.InsertQuery = InsertQuery

    def __set_layout__(self):
        layout = QVBoxLayout(self)

        boxx = QDialogButtonBox(self)

        button = QPushButton("Input Data", self)
        button2 = QPushButton("Delete")
        button3 = QPushButton("Print")
        button4 = QPushButton("Update")
        button5 = QPushButton("Show in Window")
        button6 = QPushButton("Filter By")
        button7 = QPushButton("Reset Filter")
        button8 = QPushButton("Export To")
        button_test = QPushButton("Test that shit!")

        boxx.addButton(button, boxx.ActionRole)
        boxx.addButton(button2, boxx.ActionRole)
        boxx.addButton(button3, boxx.ActionRole)
        boxx.addButton(button4, boxx.ActionRole)
        boxx.addButton(button5, boxx.ActionRole)
        boxx.addButton(button6, boxx.ActionRole)
        boxx.addButton(button7, boxx.ActionRole)
        boxx.addButton(button8, boxx.ActionRole)

        button.clicked.connect(self.__insert_show__)
        button2.clicked.connect(self.__delete_row__)
        button3.clicked.connect(self.__pdf__)
        button_test.clicked.connect(self.tests)

        self.table = Table(self.Tablename, self)

        layout.addWidget(boxx)
        layout.addWidget(self.table)
        layout.addWidget(button_test)

    def __insert_show__(self):
        # Form Button Holds the data even after exec_(),
        # use that incase of error
        form = InsertDialog(self.table.get_col_names(), [], [], self)

        form_result = form.exec_()
        if form_result:
            insert_result = self.table.insert_into_table(*form.get_input())

        while form_result and not insert_result:
            # form_result has to be true and insert result has to be false
            warn = QMessageBox()

            warn.setIcon(QMessageBox.Critical)
            warn.setStandardButtons(QMessageBox.Ok)
            warn.setWindowTitle("Error")
            warn.setText(self.table.get_last_error())
            warn.setDetailedText(self.table.__last__error__)

            warn.exec_()
            form_result = form.exec_()
            insert_result = self.table.insert_into_table(*form.get_input())

    def __delete_row__(self):
        self.table.__model__.removeRow(self.table.currentIndex().row())
        self.table.refresh()

    def __pdf__(self):
        pass

    def tests(self):
        print(self.table.get_col_names())

    def __csv__(self):
        pass

    def __update_menu__(self):
        pass

    def __view_menu__(self):
        pass

    def __filter_window__(self):
        pass

    def __reset_filter__(self):
        pass

    def __print__(self):
        pass
